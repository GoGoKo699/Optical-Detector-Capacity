"""Finite-channel and scalar checks of the additive record-rate tradeoff."""

from math import ceil, factorial, log, log2, sqrt
import unittest

import numpy as np


def g(energy):
    if energy == 0:
        return 0.0
    return (np.log1p(energy) + energy * np.log1p(1 / energy)) / log(2)


def entropy(matrix):
    eigenvalues = np.linalg.eigvalsh(matrix)
    positive = eigenvalues[eigenvalues > 1e-14]
    return -float(np.sum(positive * np.log2(positive)))


def odd_prime_at_least(dimension):
    candidate = max(3, dimension)
    if candidate % 2 == 0:
        candidate += 1
    while any(candidate % divisor == 0 for divisor in range(3, int(sqrt(candidate)) + 1, 2)):
        candidate += 2
    return candidate


def splitter(a, b, c, dimension):
    tensor = np.zeros((dimension,) * 4, dtype=complex)
    for number in range(dimension):
        for received in range(number + 1):
            for lost in range(number - received + 1):
                counted = number - received - lost
                coefficient = factorial(number) / (
                    factorial(received) * factorial(lost) * factorial(counted)
                )
                tensor[received, lost, counted, number] = sqrt(
                    coefficient * a**received * b**lost * c**counted
                )
    return tensor


def reduced_pure(tensor, keep):
    rest = tuple(index for index in range(tensor.ndim) if index not in keep)
    shape = int(np.prod([tensor.shape[index] for index in keep]))
    matrix = np.transpose(tensor, tuple(keep) + rest).reshape(shape, -1)
    return matrix @ matrix.conj().T


def finite_setting(a, b, energy_scale):
    """Evaluate all candidate settings through the full cutoff isometry."""
    dimension = ceil(energy_scale) + 1
    q = odd_prime_at_least(dimension)
    ratio = energy_scale / (1 + energy_scale)
    probabilities = ratio ** np.arange(dimension)
    probabilities /= sum(probabilities)
    isometry = splitter(a, b, 1 - a - b, dimension)
    # Purification of the average input; register order R,B,Z,D.
    pure = np.einsum("bzdr,r->rbzd", isometry, np.sqrt(probabilities))
    receiver = reduced_pure(pure, (1,))
    joint = reduced_pure(pure, (1, 3))
    loss = reduced_pure(pure, (2,))
    purity_sum = float(np.trace(receiver @ receiver).real + np.trace(joint @ joint).real)
    settings = []
    for setting in range(q):
        rows = np.exp(-2j * np.pi * (
            np.outer(np.arange(q), np.arange(dimension))
            + setting * np.arange(dimension) ** 2
        ) / q) / sqrt(q)
        np.testing.assert_allclose(rows.conj().T @ rows, np.eye(dimension), atol=2e-13)
        average_purity, coherent_information, record_probabilities = 0.0, 0.0, []
        for row in rows:
            branch = np.einsum("rbzd,d->rbz", pure, row)
            branch_receiver = reduced_pure(branch, (1,))
            branch_reference_receiver = reduced_pure(branch, (0, 1))
            probability = float(np.trace(branch_receiver).real)
            record_probabilities.append(probability)
            average_purity += float(np.trace(branch_receiver @ branch_receiver).real) / probability
            coherent_information += entropy(branch_receiver) - entropy(branch_reference_receiver)
        np.testing.assert_allclose(record_probabilities, np.full(q, 1 / q), atol=2e-13)
        settings.append((average_purity, coherent_information))
    selected = min(settings, key=lambda result: result[0])
    return {
        "q": q, "dimension": dimension, "mean": float(np.dot(probabilities, np.arange(dimension))),
        "selected_purity": selected[0], "selected_ic": selected[1],
        "purity_sum": purity_sum, "finite_bound": -log2(purity_sum) - entropy(loss),
    }


class RecordTradeoffTests(unittest.TestCase):
    def test_actual_detectors_obey_the_transcript_budget(self):
        positive_bounds = 0
        for a, b, energy, record_rate in [
            (0.8, 0.01, 4.0, 5.0),
            (0.65, 0.02, 9.0, 5.5),
            (0.2, 0.08, 10.0, 4.5),
            (0.4, 0.0, 1.0, 3.0),
        ]:
            with self.subTest(a=a, b=b, energy=energy, record_rate=record_rate):
                useful = min(energy, 1 / b if b else np.inf)
                scale = min(useful, 2 ** (record_rate - 3))
                result = finite_setting(a, b, scale)
                self.assertLess(result["mean"], scale)
                self.assertLessEqual(scale, energy)
                self.assertLess(result["q"], 2 * result["dimension"])
                self.assertLess(log2(result["q"] + 1), record_rate)
                self.assertLessEqual(ceil(100 * log2(result["q"] + 1)), 100 * record_rate)
                self.assertLessEqual(result["selected_purity"], result["purity_sum"] + 2e-12)
                self.assertGreaterEqual(result["selected_ic"], result["finite_bound"] - 2e-12)
                self.assertGreaterEqual(result["finite_bound"], log2(scale) + log2(a) - 4 - 2e-12)
                if result["finite_bound"] > 0.3:
                    positive_bounds += 1
        self.assertGreaterEqual(positive_bounds, 1)

    def test_uniform_constants_and_nonvacuous_large_scale_bounds(self):
        positive_tradeoff_bounds = 0
        for a in (0.2, 0.49, 0.8):
            constant_lower = 7 + log2(1 / a)
            baseline_ceiling = max(0, log2(a / (1 - a)))
            constant_upper = max(baseline_ceiling, g(a))
            for energy, b in [(1.0, 0.0), (4.0, 0.01), (1e6, 0.0), (1e8, 1e-4), (1e12, 1e-13)]:
                useful = min(energy, 1 / b if b else np.inf)
                collective = g(a * energy) - g(b * energy)
                baseline = max(0, g(a * energy) - g((1 - a) * energy))
                for record_rate in (0, 1, 2.999, 3, 5, 10, 20, 40):
                    with self.subTest(a=a, energy=energy, b=b, record_rate=record_rate):
                        target = min(record_rate, log2(useful))
                        lower = max(baseline, target - constant_lower)
                        upper = min(collective, baseline + record_rate)
                        self.assertLessEqual(lower, upper + 2e-12)
                        self.assertLessEqual(upper, target + constant_upper + 2e-12)
                        if record_rate < 3:
                            self.assertLess(target - constant_lower, 0)
                            continue
                        scale = min(useful, 2 ** (record_rate - 3))
                        dimension = ceil(scale) + 1
                        tail = np.exp(-dimension * np.log1p(1 / scale))
                        self.assertLess(tail, 0.5)
                        self.assertLessEqual(b * scale, 1 + 2e-14)
                        self.assertLess(log2(7 * scale), record_rate)
                        self.assertLessEqual(ceil(100 * log2(7 * scale)), 100 * record_rate)
                        purity_bound = (1 / (1 + 2 * a * scale) + 1 / (1 + 2 * (1 - b) * scale)) / (1 - tail) ** 2
                        achieved_bound = -log2(purity_bound) - g(b * scale)
                        self.assertGreaterEqual(achieved_bound, target - constant_lower - 2e-12)
                        if target - constant_lower > 1:
                            positive_tradeoff_bounds += 1
        self.assertGreater(positive_tradeoff_bounds, 10)


if __name__ == "__main__":
    unittest.main()
