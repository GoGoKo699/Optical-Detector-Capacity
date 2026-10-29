"""Full-isometry checks of the local-invariance reference-spread converse."""

from math import ceil, factorial, log, log2, pi, sqrt
import unittest

import numpy as np


def entropy(matrix):
    values = np.linalg.eigvalsh(matrix)
    values = values[values > 1e-14]
    return -float(np.sum(values * np.log2(values)))


def shannon(values):
    values = np.asarray(values)
    positive = values[values > 1e-14]
    return -float(np.sum(positive * np.log2(positive)))


def g(energy):
    if energy == 0:
        return 0.0
    return (np.log1p(energy) + energy * np.log1p(1 / energy)) / log(2)


def marginal(pure, keep):
    other = tuple(index for index in range(pure.ndim) if index not in keep)
    dimension = int(np.prod([pure.shape[index] for index in keep]))
    matrix = np.transpose(pure, tuple(keep) + other).reshape(dimension, -1)
    return matrix @ matrix.conj().T


def splitter(a, b, c, dimension):
    tensor = np.zeros((dimension,) * 4, dtype=complex)
    for number in range(dimension):
        for j in range(number + 1):
            for lost in range(number - j + 1):
                collected = number - j - lost
                coefficient = factorial(number) / (factorial(j) * factorial(lost) * factorial(collected))
                tensor[j, lost, collected, number] = sqrt(
                    coefficient * a**j * b**lost * c**collected
                )
    return tensor


def setup_state(seed, a, b, c, width=3, offset=1):
    rng = np.random.default_rng(seed)
    raw_encoder = rng.normal(size=(6, 2)) + 1j * rng.normal(size=(6, 2))
    encoding, _ = np.linalg.qr(raw_encoder)
    # A CPTP encoder with actual reference R, discarded ancilla F, and input A.
    encoded = np.transpose(encoding.reshape(3, 2, 2), (2, 1, 0)) / sqrt(2)
    sigma_input = marginal(encoded, (2,))
    raw_reference = rng.normal(size=(width, width)) + 1j * rng.normal(size=(width, width))
    sigma_reference = raw_reference @ raw_reference.conj().T
    sigma_reference /= np.trace(sigma_reference)
    values, vectors = np.linalg.eigh(sigma_reference)
    # G is a mathematical purification; it is not provided to the receiver.
    reference = np.zeros((width, width + offset), dtype=complex)
    for index in range(width):
        reference[index, offset:] = sqrt(max(0, values[index])) * vectors[:, index]
    split = np.einsum("rfa,bzda->rfbzd", encoded, splitter(a, b, c, 3))
    joint = np.einsum("rfbzd,gw->rfbzdgw", split, reference)
    return joint, sigma_input, marginal(reference, (1,)), rng


def invariant_sector_rows(detector_dimension, reference_dimension, rng):
    rows = []
    for total in range(detector_dimension + reference_dimension - 1):
        sector = [(d, w) for d in range(detector_dimension) for w in range(reference_dimension) if d + w == total]
        size = len(sector)
        raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
        basis, _ = np.linalg.qr(raw)
        for outcome in range(size):
            vector = np.zeros((detector_dimension, reference_dimension), dtype=complex)
            for component, (d, w) in enumerate(sector):
                vector[d, w] = basis[component, outcome]
            rows.append((total, outcome, vector))
    return rows


class ReferenceWidthTests(unittest.TestCase):
    def test_coherent_input_mixed_reference_and_sector_refinement(self):
        coherence_effect_seen = False
        for seed, a, b in [(12, 0.3, 0.1), (49, 0.7, 0.1), (77, 0.2, 0.05)]:
            with self.subTest(seed=seed, a=a, b=b):
                c = 1 - a - b
                pure, input_state, reference_state, rng = setup_state(seed, a, b, c)
                self.assertGreater(np.linalg.norm(input_state - np.diag(np.diag(input_state))), 0.05)
                self.assertGreater(np.linalg.norm(reference_state - np.diag(np.diag(reference_state))), 0.05)
                np.testing.assert_allclose(marginal(pure, (0,)), np.eye(2) / 2, atol=2e-14)
                detector_dimension, reference_dimension = pure.shape[4], pure.shape[6]
                total_dimension = detector_dimension + reference_dimension - 1
                rows = invariant_sector_rows(detector_dimension, reference_dimension, rng)
                effects = [np.outer(row.ravel(), row.ravel().conj()) for _, _, row in rows]
                np.testing.assert_allclose(sum(effects), np.eye(detector_dimension * reference_dimension), atol=2e-14)
                total_operator = np.diag([d + w for d in range(detector_dimension) for w in range(reference_dimension)])
                for effect in effects:
                    np.testing.assert_allclose(effect @ total_operator, total_operator @ effect, atol=2e-14)

                p_joint = np.zeros((3, total_dimension))
                coarse_b = [np.zeros((3, 3), complex) for _ in range(2)]
                coarse_rb = [np.zeros((6, 6), complex) for _ in range(2)]
                fine_ic, conditional_b, conditional_j = 0.0, 0.0, 0.0
                actual_fine_probabilities, diagonal_fine_probabilities = [], []
                input_numbers = np.diag(input_state).real
                reference_numbers = np.diag(reference_state).real
                classical = np.zeros((3, detector_dimension, reference_dimension))
                optical = splitter(a, b, c, 3)
                for j in range(3):
                    for collected in range(detector_dimension):
                        count_probability = sum(input_numbers[n] * sum(abs(optical[j, lost, collected, n]) ** 2 for lost in range(3)) for n in range(3))
                        classical[j, collected, :] = count_probability * reference_numbers
                for total, outcome, row in rows:
                    branch = np.einsum("rfbzdgw,dw->rfbzg", pure, row.conj())
                    receiver = marginal(branch, (2,))
                    logical_receiver = marginal(branch, (0, 2))
                    probability = float(np.trace(receiver).real)
                    coarse_b[outcome % 2] += receiver
                    coarse_rb[outcome % 2] += logical_receiver
                    p_joint[:, total] += np.diag(receiver).real
                    actual_fine_probabilities.append(probability)
                    diagonal_fine_probabilities.append(float(np.sum(classical * abs(row)[None, :, :] ** 2)))
                    if probability > 1e-14:
                        fine_ic += entropy(receiver) - entropy(logical_receiver)
                        conditional_b += probability * entropy(receiver / probability)
                        conditional_j += probability * shannon(np.diag(receiver).real / probability)
                coarse_ic = sum(entropy(x) - entropy(y) for x, y in zip(coarse_b, coarse_rb))
                self.assertLessEqual(coarse_ic, fine_ic + 3e-12)
                self.assertLessEqual(fine_ic, conditional_b + 3e-12)
                self.assertLessEqual(conditional_b, conditional_j + 3e-12)
                self.assertAlmostEqual(float(np.sum(p_joint)), 1, places=13)
                predicted_joint = np.zeros_like(p_joint)
                for collected in range(detector_dimension):
                    for w in range(reference_dimension):
                        predicted_joint[:, collected + w] += classical[:, collected, w]
                np.testing.assert_allclose(p_joint, predicted_joint, atol=3e-14)
                if np.linalg.norm(np.array(actual_fine_probabilities) - diagonal_fine_probabilities, ord=1) > 1e-3:
                    coherence_effect_seen = True

                energy = float(np.dot(np.arange(3), input_numbers))
                mean_w = float(np.dot(np.arange(reference_dimension), reference_numbers))
                variance_w = float(np.dot((np.arange(reference_dimension) - mean_w) ** 2, reference_numbers))
                mse = sum(p_joint[j, total] * (j - a / c * (total - mean_w)) ** 2 for j in range(3) for total in range(total_dimension))
                predicted_mse = a * (a + c) / c * energy + (a / c) ** 2 * variance_w
                self.assertAlmostEqual(float(mse), predicted_mse, places=12)
                conditional_variance, conditional_entropy = 0.0, 0.0
                for total in range(total_dimension):
                    probability = float(sum(p_joint[:, total]))
                    if probability > 1e-14:
                        distribution = p_joint[:, total] / probability
                        mean_j = float(np.dot(np.arange(3), distribution))
                        conditional_variance += probability * float(np.dot((np.arange(3) - mean_j) ** 2, distribution))
                        conditional_entropy += probability * shannon(distribution)
                self.assertLessEqual(conditional_j, conditional_entropy + 3e-12)
                self.assertLessEqual(conditional_variance, mse + 3e-12)
                entropy_bound = 0.5 * log2(2 * pi * np.e * (predicted_mse + 1 / 12))
                self.assertLessEqual(conditional_entropy, entropy_bound + 3e-12)
                self.assertLessEqual(coarse_ic, entropy_bound + 3e-12)
                # Width is three consecutive levels, independently of the offset.
                self.assertLessEqual(variance_w, (3 - 1) ** 2 / 4 + 3e-14)
        # Fine outcomes do depend on coherences: only the J,T marginal is classical.
        self.assertTrue(coherence_effect_seen)

    def test_global_conservation_does_not_imply_local_invariance(self):
        vector = np.array([0, 1, 1, 0], dtype=complex) / sqrt(2)
        effect = np.outer(vector, vector.conj())
        local_one = np.diag([0, 0, 1, 1])
        local_two = np.diag([0, 1, 0, 1])
        total = local_one + local_two
        np.testing.assert_allclose(effect @ total, total @ effect, atol=1e-14)
        self.assertGreater(np.linalg.norm(effect @ local_one - local_one @ effect), 0.5)
        self.assertGreater(np.linalg.norm(effect @ local_two - local_two @ effect), 0.5)

    def test_width_profile_scalar_regression(self):
        nonvacuous = 0
        reference_penalty = g(5 * pi * pi / 48)
        for a in (0.2, 0.49, 0.8):
            for energy in (1, 4, 32, 1e4, 1e8):
                for width in (1, 2, 4, 8, 128, 100000):
                    b = min(0.25 * min(a, 1 - a), 0.5 / energy)
                    c = 1 - a - b
                    profile = min(log2(energy), max(0.5 * log2(energy), log2(width)))
                    variance_ceiling = (width - 1) ** 2 / 4
                    upper = min(g(a * energy) - g(b * energy), 0.5 * log2(2 * pi * np.e * (a * (a + c) * energy / c + (a / c) ** 2 * variance_ceiling + 1 / 12)))
                    self.assertTrue(np.isfinite(upper))
                    if width < 4:
                        self.assertLessEqual(profile - 0.5 * log2(energy), 2)
                        continue
                    scale = min(energy, width / 4)
                    dimension = ceil(scale) + 1
                    ratio = (dimension - 1) / (width + 1)
                    self.assertLessEqual(ratio, 0.5)
                    tail = np.exp(-dimension * np.log1p(1 / scale))
                    purity = (1 / (1 + 2 * a * scale) + 1 / (1 + 2 * (1 - b) * scale)) / (1 - tail) ** 2
                    actual_lower = -log2(purity) - g(b * scale) - g(pi * pi / 12 * (2 * ratio + ratio * ratio))
                    conservative = min(log2(energy), log2(width)) - (6 + log2(1 / a) + reference_penalty)
                    self.assertGreaterEqual(actual_lower, conservative - 3e-12)
                    self.assertLessEqual(conservative, upper + 3e-12)
                    if conservative > 1:
                        nonvacuous += 1
        self.assertGreater(nonvacuous, 5)

    def test_variance_does_not_lower_bound_mean_reference_energy(self):
        for distant_level in (10, 1000, 1000000):
            probability = 1 / distant_level
            mean = probability * distant_level
            variance = probability * (distant_level - mean) ** 2 + (1 - probability) * mean**2
            self.assertEqual(mean, 1)
            self.assertAlmostEqual(variance, distant_level - 1, places=8)


if __name__ == "__main__":
    unittest.main()
