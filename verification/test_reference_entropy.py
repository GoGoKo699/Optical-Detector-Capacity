"""Finite checks of the shifted-sine entropy lemma and its resource constants."""
from __future__ import annotations

import math
import unittest

import numpy as np

import verify


def translated_sines(width: int, shifts: int) -> np.ndarray:
    """Columns are ordinary zero-padded translations, with no cyclic wrap."""
    amplitude = (math.sqrt(2 / (width + 1))
                 * np.sin(math.pi * np.arange(1, width + 1) / (width + 1)))
    vectors = np.zeros((width + shifts - 1, shifts))
    for k in range(shifts):
        vectors[k:k + width, k] = amplitude
    return vectors


def dirichlet_laplacian(length: int) -> np.ndarray:
    return (2 * np.eye(length) - np.eye(length, k=1) - np.eye(length, k=-1))


def entropy_parameters(width: int, shifts: int) -> tuple[float, float]:
    """Exact mode-mean upper bound and its simpler ratio upper bound."""
    length = width + shifts - 1
    sine_energy = 4 * math.sin(math.pi / (2 * (width + 1)))**2
    ground_energy = 4 * math.sin(math.pi / (2 * (length + 1)))**2
    mu = (length + 1)**2 * (sine_energy - ground_energy) / 12
    ratio = (shifts - 1) / (width + 1)
    upper = math.pi**2 * (2 * ratio + ratio**2) / 12
    return max(0.0, mu), upper


def sufficient_width(shifts: int, beta: float) -> tuple[int, float]:
    """Invert g numerically only to test the explicit analytical width choice."""
    low, high = 0.0, 1.0
    while verify.g(high) < beta:
        high *= 2
    for _ in range(150):
        middle = (low + high) / 2
        if verify.g(middle) < beta:
            low = middle
        else:
            high = middle
    inverse = (low + high) / 2
    # Equivalent to sqrt(1 + 12*g^{-1}(beta)/pi^2)-1, without cancellation.
    ratio = math.expm1(math.log1p(12 * inverse / math.pi**2) / 2)
    width = max(1, math.ceil((shifts - 1) / ratio) - 1)
    return width, ratio


class ShiftedReferenceEntropyChecks(unittest.TestCase):
    def assert_close(self, left, right, atol: float = 2e-11):
        np.testing.assert_allclose(left, right, atol=atol, rtol=0)

    def test_dirichlet_spectrum_and_mode_gap(self):
        for length in range(2, 41):
            laplacian = dirichlet_laplacian(length)
            eigenvalues = np.linalg.eigvalsh(laplacian)
            mode = np.arange(1, length + 1)
            expected = 4 * np.sin(math.pi * mode / (2 * (length + 1)))**2
            with self.subTest(length=length):
                self.assert_close(eigenvalues, expected)
                gaps = eigenvalues[1:] - eigenvalues[0]
                lower = 12 * np.arange(1, length) / (length + 1)**2
                self.assertTrue(np.all(gaps >= lower - 2e-13))

    def test_arbitrary_shift_weights_and_entropy(self):
        rng = np.random.default_rng(20261029)
        for width, shifts in ((1, 2), (1, 5), (2, 2), (2, 7),
                              (3, 5), (5, 3), (9, 9), (17, 5)):
            vectors = translated_sines(width, shifts)
            length = width + shifts - 1
            laplacian = dirichlet_laplacian(length)
            eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
            delta = 4 * math.sin(math.pi / (2 * (width + 1)))**2
            mu, upper = entropy_parameters(width, shifts)
            weights = [np.full(shifts, 1 / shifts),
                       np.eye(shifts)[0], np.eye(shifts)[-1],
                       rng.dirichlet(np.ones(shifts)),
                       rng.dirichlet(np.full(shifts, .15))]
            with self.subTest(width=width, shifts=shifts):
                self.assert_close(np.sum(vectors**2, axis=0), np.ones(shifts))
                self.assert_close(np.einsum('ik,ij,jk->k', vectors, laplacian, vectors),
                                  np.full(shifts, delta))
                self.assertLessEqual(mu, upper + 2e-12)
                for p in weights:
                    rho = (vectors * p) @ vectors.T
                    self.assert_close(np.trace(rho), 1)
                    self.assert_close(np.trace(laplacian @ rho), delta)
                    mode_probabilities = np.diag(eigenvectors.T @ rho @ eigenvectors)
                    mode_mean = float(np.dot(np.arange(length), mode_probabilities))
                    self.assertLessEqual(mode_mean, mu + 2e-11)
                    quantum_entropy = verify.von_neumann(rho)
                    mode_entropy = verify.entropy(mode_probabilities)
                    self.assertLessEqual(quantum_entropy, mode_entropy + 2e-11)
                    self.assertLessEqual(mode_entropy, verify.g(mu) + 2e-11)
                    self.assertLessEqual(quantum_entropy, verify.g(upper) + 2e-11)

    def test_explicit_width_for_requested_penalty(self):
        for shifts in (2, 3, 8, 31):
            for beta in (1., .5, .1, .01):
                width, ratio = sufficient_width(shifts, beta)
                mu, upper = entropy_parameters(width, shifts)
                with self.subTest(shifts=shifts, beta=beta):
                    self.assertGreaterEqual(width, 1)
                    self.assertLessEqual((shifts - 1) / (width + 1), ratio + 1e-14)
                    self.assertLessEqual(verify.g(upper), beta + 2e-12)
                    self.assertLessEqual(mu, upper + 2e-12)
                    # h cancels from the initial-reference-stock inequality.
                    self.assertLessEqual((width - 1) / 2,
                                         (shifts - 1) / (2 * ratio))

    def test_constant_ratio_and_vanishing_penalty(self):
        for shifts in (2, 3, 10, 100):
            _, upper = entropy_parameters(shifts, shifts)
            self.assertLessEqual(upper, math.pi**2 / 4)
            penalties = [verify.g(entropy_parameters(multiplier * shifts, shifts)[1])
                         for multiplier in (1, 2, 4, 16, 256)]
            self.assertTrue(all(a > b for a, b in zip(penalties, penalties[1:])))
            self.assertLess(penalties[-1], .11)


if __name__ == '__main__':
    unittest.main()
