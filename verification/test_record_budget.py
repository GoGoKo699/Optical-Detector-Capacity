"""Finite optical checks of the classical-record converse.

The written proof covers arbitrary dimensions and codes. These checks build the
complete isometry, keep discarded encoder ancillas, and evaluate actual reference
states instead of identifying a mixed encoder with an input purification.
"""

from math import factorial, sqrt
import unittest

import numpy as np


def entropy(matrix):
    values = np.linalg.eigvalsh(matrix)
    positive = values[values > 1e-14]
    return -float(np.sum(positive * np.log2(positive)))


def g(energy):
    if energy == 0:
        return 0.0
    return (energy + 1) * np.log2(energy + 1) - energy * np.log2(energy)


def marginal(pure, keep):
    other = tuple(axis for axis in range(pure.ndim) if axis not in keep)
    reordered = np.transpose(pure, tuple(keep) + other)
    dimension = int(np.prod([pure.shape[axis] for axis in keep]))
    matrix = reordered.reshape(dimension, -1)
    return matrix @ matrix.conj().T


def splitter(a, b, c, dimension=3):
    result = np.zeros((dimension,) * 4, dtype=complex)
    for number in range(dimension):
        for received in range(number + 1):
            for lost in range(number - received + 1):
                counted = number - received - lost
                coefficient = factorial(number) / (
                    factorial(received) * factorial(lost) * factorial(counted)
                )
                result[received, lost, counted, number] = sqrt(
                    coefficient * a**received * b**lost * c**counted
                )
    return result


def encoded_state(seed, input_dimension=3, ancilla_dimension=2, logical_dimension=2):
    """Purification R,F,A of a CPTP encoder with its ancilla F discarded."""
    rng = np.random.default_rng(seed)
    raw = rng.normal(size=(input_dimension * ancilla_dimension, logical_dimension))
    raw = raw + 1j * rng.normal(size=raw.shape)
    isometry, _ = np.linalg.qr(raw)
    return np.transpose(
        isometry.reshape(input_dimension, ancilla_dimension, logical_dimension),
        (2, 1, 0),
    ) / sqrt(logical_dimension)


def through_splitter(encoder, a, b, c):
    return np.einsum("rfa,bzda->rfbzd", encoder, splitter(a, b, c))


def flagged_matrix(branches):
    dimension = branches[0].shape[0]
    output = np.zeros((len(branches) * dimension,) * 2, dtype=complex)
    for number, branch in enumerate(branches):
        interval = slice(number * dimension, (number + 1) * dimension)
        output[interval, interval] = branch
    return output


def measured_states(pure):
    dimension = pure.shape[-1]
    rows = np.exp(2j * np.pi * np.outer(np.arange(dimension), np.arange(dimension)) / dimension)
    rows /= sqrt(dimension)
    receiver, reference_receiver, loss, full_complement, probabilities = [], [], [], [], []
    for row in rows:
        branch = np.einsum("rfbzd,d->rfbz", pure, row.conj())
        receiver.append(marginal(branch, (2,)))
        reference_receiver.append(marginal(branch, (0, 2)))
        loss.append(marginal(branch, (3,)))
        full_complement.append(marginal(branch, (1, 3)))
        probabilities.append(float(np.vdot(branch, branch).real))
    return receiver, reference_receiver, loss, full_complement, np.array(probabilities)


class RecordBudgetTests(unittest.TestCase):
    def test_record_increment_with_mixed_encoders(self):
        for seed in (8, 19, 61):
            encoder = encoded_state(seed)
            np.testing.assert_allclose(marginal(encoder, (0,)), np.eye(2) / 2, atol=2e-14)
            input_state = marginal(encoder, (2,))
            energy = float(np.dot(np.arange(3), np.diag(input_state).real))
            for a in (0.2, 0.5, 0.7):
                with self.subTest(seed=seed, received_fraction=a):
                    pure = through_splitter(encoder, a, 0.1, 0.9 - a)
                    receiver = marginal(pure, (2,))
                    reference_receiver = marginal(pure, (0, 2))
                    ic_before = entropy(receiver) - entropy(reference_receiver)
                    bs, rbs, zs, fzs, probabilities = measured_states(pure)
                    np.testing.assert_allclose(sum(bs), receiver, atol=2e-14)
                    np.testing.assert_allclose(sum(rbs), reference_receiver, atol=2e-14)
                    self.assertAlmostEqual(float(sum(probabilities)), 1, places=13)
                    record_entropy = -float(np.sum(probabilities * np.log2(probabilities)))
                    ic_after = entropy(flagged_matrix(bs)) - entropy(flagged_matrix(rbs))
                    complement_expression = entropy(flagged_matrix(bs)) - entropy(flagged_matrix(fzs))
                    self.assertAlmostEqual(ic_after, complement_expression, places=12)
                    increment = ic_after - ic_before
                    self.assertGreaterEqual(increment, -2e-12)
                    self.assertLessEqual(increment, record_entropy + 2e-12)
                    if a <= 0.5:
                        self.assertLessEqual(ic_before, 2e-12)
                        self.assertLessEqual(ic_after, record_entropy + 2e-12)
                    else:
                        # RF purifies the input; R alone is the actual logical reference.
                        ic_purified_input = entropy(receiver) - entropy(marginal(pure, (3, 4)))
                        self.assertLessEqual(ic_before, ic_purified_input + 2e-12)
                        capacity_bound = g(a * energy) - g((1 - a) * energy)
                        self.assertLessEqual(ic_purified_input, capacity_bound + 2e-12)
                        self.assertLessEqual(ic_after, capacity_bound + record_entropy + 2e-12)
                    # Omitting F changes the logical coherent information for these encoders.
                    wrong_reference = entropy(flagged_matrix(bs)) - entropy(flagged_matrix(zs))
                    self.assertGreater(wrong_reference - ic_after, 1e-3)

    def test_antidegradable_symmetric_reference_extension(self):
        encoder = encoded_state(42)
        for a in (0.2, 0.45, 0.5):
            with self.subTest(received_fraction=a):
                original = through_splitter(encoder, a, 0.1, 0.9 - a)
                extension = through_splitter(encoder, a, a, 1 - 2 * a)
                rb = marginal(extension, (0, 2))
                rb_copy = marginal(extension, (0, 3))
                np.testing.assert_allclose(rb, rb_copy, atol=2e-14)
                np.testing.assert_allclose(rb, marginal(original, (0, 2)), atol=2e-14)
                conditional_entropy = entropy(rb) - entropy(marginal(extension, (2,)))
                self.assertGreaterEqual(conditional_entropy, -2e-12)

    def test_discarding_the_record_changes_the_complement(self):
        # A pure encoder isolates loss of the helper record from discarded F.
        encoder = np.zeros((3, 1, 3), dtype=complex)
        for number in range(3):
            encoder[number, 0, number] = 1 / sqrt(3)
        pure = through_splitter(encoder, 0.4, 0.05, 0.55)
        bs, rbs, zs, _, _ = measured_states(pure)
        # Coarse-grain all helper outcomes to a constant Y.
        receiver, reference_receiver = sum(bs), sum(rbs)
        actual = entropy(receiver) - entropy(reference_receiver)
        whole_lost_field = marginal(pure, (3, 4))
        self.assertAlmostEqual(actual, entropy(receiver) - entropy(whole_lost_field), places=12)
        self.assertLess(actual, 0)
        # Treating Z alone as the complement spuriously gives a positive value.
        incorrect = entropy(receiver) - entropy(sum(zs))
        self.assertGreater(incorrect, 0.2)
        self.assertGreater(incorrect - actual, 0.2)


if __name__ == "__main__":
    unittest.main()
