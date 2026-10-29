"""Independent splitter-contraction check and exact-certificate regression."""

from fractions import Fraction as F
import importlib.util
import json
from math import factorial, sqrt
from pathlib import Path
import subprocess
import sys
import unittest

import numpy as np


CERTIFICATE_PATH = Path(__file__).with_name("qutrit_certificate.py")
SPEC = importlib.util.spec_from_file_location("qutrit_certificate", CERTIFICATE_PATH)
certificate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(certificate)


def splitter_isometry(a, b, c):
    """Build V independently from multinomial amplitudes, output order B,Z,D."""
    result = np.zeros((3, 3, 3, 3), dtype=complex)
    for number in range(3):
        for received in range(number + 1):
            for lost in range(number - received + 1):
                counted = number - received - lost
                multiplicity = factorial(number) / (
                    factorial(received) * factorial(lost) * factorial(counted)
                )
                probability = multiplicity * a**received * b**lost * c**counted
                result[received, lost, counted, number] = sqrt(probability)
    return result


def subnormalized_entropy(matrix):
    eigenvalues = np.linalg.eigvalsh(matrix)
    positive = eigenvalues[eigenvalues > 1e-15]
    return -float(np.sum(positive * np.log2(positive)))


class QutritBridgeTests(unittest.TestCase):
    def test_branch_formulas_against_full_isometry(self):
        a, b, c = F(1, 5), F(2, 25), F(18, 25)
        p = (F(0), F(1, 2), F(1, 2))
        isometry = splitter_isometry(float(a), float(b), float(c))
        flat = isometry.reshape(27, 3)
        np.testing.assert_allclose(flat.conj().T @ flat, np.eye(3), atol=2e-15)
        rows = np.array([[0, 1, 0], [1 / sqrt(2), 0, 1 / sqrt(2)], [1 / sqrt(2), 0, -1 / sqrt(2)]])
        np.testing.assert_allclose(rows.conj().T @ rows, np.eye(3), atol=2e-15)
        probability = np.array([float(value) for value in p])
        total_information = 0.0
        total_probability = 0.0
        for outcome, row in enumerate(rows):
            branch = np.einsum("d,bzda->bza", row, isometry)
            receiver = np.einsum("bzn,n,czn->bc", branch, probability, branch.conj())
            inaccessible = np.einsum("bzn,n,bwn->zw", branch, probability, branch.conj())
            self.assertAlmostEqual(float(np.trace(receiver).real), float(np.trace(inaccessible).real), places=14)
            total_probability += float(np.trace(receiver).real)
            total_information += subnormalized_entropy(receiver) - subnormalized_entropy(inaccessible)
            for actual, t, u in [(receiver, a, b), (inaccessible, b, a)]:
                entries = certificate.branch_entries(t, u, c, p)
                if outcome == 0:
                    expected = np.diag([float(x) for x in entries["one"]] + [0])
                else:
                    off_diagonal = (1 if outcome == 1 else -1) * sqrt(float(entries["off_squared"]))
                    expected = np.array([
                        [float(entries["d0"]), 0, off_diagonal],
                        [0, float(entries["d1"]), 0],
                        [off_diagonal, 0, float(entries["d2"])],
                    ])
                np.testing.assert_allclose(actual, expected, atol=2e-15, rtol=2e-14)
        self.assertAlmostEqual(total_probability, 1, places=14)
        report = certificate.certificate()
        self.assertAlmostEqual(total_information, report["witness_rate_interval_diagnostic"][0], places=13)
        self.assertGreater(total_information, 0.329)

    def test_exact_certificate_with_python_optimization(self):
        completed = subprocess.run(
            [sys.executable, "-O", str(CERTIFICATE_PATH)],
            check=True, capture_output=True, text=True,
        )
        report = json.loads(completed.stdout)
        self.assertTrue(report["exact_arithmetic_assertions_passed"])
        self.assertEqual(report["counting_capacity_strict_upper"], "0.318")
        self.assertEqual(report["witness_rate_strict_lower"], "0.329")
        self.assertEqual(report["separation_strict_lower"], "0.011")
        self.assertIn("no full-Fock comparison", report["claim_scope"])


if __name__ == "__main__":
    unittest.main()
