"""Finite checks of the number-conserving detector-width proof."""

from fractions import Fraction
from itertools import combinations, product
from math import comb, prod, sqrt
import unittest

import numpy as np


TOL = 2e-13


def sector(modes, photons):
    """Enumerate occupations in the fixed-total Fock basis."""
    end = photons + modes - 1
    for bars in combinations(range(end), modes - 1):
        cuts = (-1, *bars, end)
        yield tuple(right - left - 1 for left, right in zip(cuts, cuts[1:]))


def projected_splitter(modes, receiver_total, helper_total):
    """Return the normalized splitter component indexed by B, D, and input."""
    inputs = {occupation: index for index, occupation in enumerate(
        sector(modes, receiver_total + helper_total)
    )}
    receiver = tuple(sector(modes, receiver_total))
    helper = tuple(sector(modes, helper_total))
    basis = np.zeros((len(receiver), len(helper), len(inputs)))
    normalizer = comb(receiver_total + helper_total, helper_total)
    for row, received in enumerate(receiver):
        for column, detected in enumerate(helper):
            incident = tuple(j + k for j, k in zip(received, detected))
            weight = prod(comb(n, j) for n, j in zip(incident, received))
            basis[row, column, inputs[incident]] = sqrt(weight / normalizer)
    return basis


class DetectorWidthTests(unittest.TestCase):
    def test_projected_splitter_and_uniform_marginals(self):
        for modes, j, k in product(range(1, 5), range(4), range(4)):
            with self.subTest(modes=modes, receiver=j, helper=k):
                basis = projected_splitter(modes, j, k)
                receiver_dim, helper_dim, input_dim = basis.shape
                self.assertEqual(receiver_dim, comb(j + modes - 1, modes - 1))
                self.assertEqual(helper_dim, comb(k + modes - 1, modes - 1))
                self.assertEqual(input_dim, comb(j + k + modes - 1, modes - 1))
                isometry = basis.reshape(-1, input_dim)
                np.testing.assert_allclose(
                    isometry.T @ isometry, np.eye(input_dim), atol=TOL, rtol=0
                )
                receiver = np.einsum("bdi,cdi->bc", basis, basis) / input_dim
                helper = np.einsum("bdi,bei->de", basis, basis) / input_dim
                np.testing.assert_allclose(
                    receiver, np.eye(receiver_dim) / receiver_dim, atol=TOL, rtol=0
                )
                np.testing.assert_allclose(
                    helper, np.eye(helper_dim) / helper_dim, atol=TOL, rtol=0
                )

    def test_sector_fourier_phase_purity(self):
        for modes, k in ((2, 1), (2, 2), (3, 1)):
            with self.subTest(modes=modes, helper=k):
                states = []
                weights = (0.3, 0.2, 0.35, 0.15)
                for j in range(len(weights)):
                    basis = projected_splitter(modes, j, k)
                    joint = np.einsum("bdi,cei->bdce", basis, basis) / basis.shape[2]
                    states.append(joint)
                helper_dim = states[0].shape[1]
                expected_purity = 0.0
                for weight, joint in zip(weights, states):
                    receiver_dim = joint.shape[0]
                    matrix = joint.reshape(receiver_dim * helper_dim, -1)
                    receiver = np.trace(joint, axis1=1, axis2=3)
                    diagonal_purity = sum(
                        np.linalg.norm(joint[:, d, :, d], "fro")**2
                        for d in range(helper_dim)
                    )
                    expected_purity += weight**2 * (
                        np.linalg.norm(receiver, "fro")**2
                        + np.linalg.norm(matrix, "fro")**2
                        - diagonal_purity
                    )
                fourier = np.exp(
                    2j * np.pi * np.outer(np.arange(helper_dim), np.arange(helper_dim))
                    / helper_dim
                )
                setting_purities = []
                for mask in product((1, 1j, -1, -1j), repeat=helper_dim):
                    outcome_purities = []
                    # Vectors have squared norm d. Since the helper marginal is
                    # I/d, this directly produces a normalized conditional state.
                    for vector in fourier * mask:
                        purity = 0.0
                        for weight, joint in zip(weights, states):
                            receiver = np.einsum("d,bdce,e->bc", vector.conj(), joint, vector)
                            self.assertAlmostEqual(float(np.trace(receiver).real), 1)
                            purity += weight**2 * np.linalg.norm(receiver, "fro")**2
                        outcome_purities.append(purity)
                    setting_purities.append(np.mean(outcome_purities))
                self.assertAlmostEqual(float(np.mean(setting_purities)), expected_purity, delta=TOL)
                self.assertLessEqual(min(setting_purities), expected_purity + TOL)

    def test_thermal_conditional_count(self):
        # Convolve the exact one-mode count law independently of the
        # block negative-binomial formula, using rational probabilities.
        cutoff = 6
        totals = tuple(product(range(cutoff + 1), repeat=2))
        for a, c, energy in (
            (Fraction(1, 4), Fraction(3, 4), 1),
            (Fraction(1, 2), Fraction(1, 4), 8),
            (Fraction(1, 10), Fraction(4, 5), 13),
        ):
            normalizer = 1 + (a + c) * energy
            one_mode = {
                (j, k): comb(j + k, j) * (a * energy)**j * (c * energy)**k
                / normalizer**(j + k + 1)
                for j, k in totals
            }
            distribution = {(0, 0): Fraction(1)}
            for modes in range(1, 5):
                distribution = {
                    (j, k): sum(
                        distribution.get((j - jj, k - kk), 0) * one_mode[jj, kk]
                        for jj in range(j + 1) for kk in range(k + 1)
                    )
                    for j, k in totals
                }
                conditional_mean = a * energy / (1 + c * energy)
                for j, k in totals:
                    with self.subTest(a=a, c=c, energy=energy, modes=modes, j=j, k=k):
                        k_probability = (
                            comb(k + modes - 1, k) * (c * energy)**k
                            / (1 + c * energy)**(k + modes)
                        )
                        j_given_k = (
                            comb(j + k + modes - 1, j) * conditional_mean**j
                            / (1 + conditional_mean)**(j + k + modes)
                        )
                        self.assertEqual(distribution[j, k] / k_probability, j_given_k)

    def test_thinning_reciprocal_and_sector_dimension(self):
        for j, retention in product(range(21), (Fraction(1, 20), Fraction(1, 3), Fraction(1))):
            with self.subTest(receiver=j, retention=retention):
                reciprocal = sum(
                    Fraction(j + 1, w + 1) * comb(j, w)
                    * retention**w * (1 - retention)**(j - w)
                    for w in range(j + 1)
                )
                self.assertEqual(reciprocal, (1 - (1 - retention)**(j + 1)) / retention)
                self.assertLessEqual(reciprocal, 1 / retention)
        for modes, j in product(range(1, 9), range(21)):
            for w in range(j + 1):
                with self.subTest(modes=modes, receiver=j, inaccessible=w):
                    ratio = Fraction(comb(j + modes - 1, modes - 1), comb(w + modes - 1, modes - 1))
                    self.assertLessEqual(ratio, Fraction(j + 1, w + 1)**(modes - 1))


if __name__ == "__main__":
    unittest.main()
