"""Regressions for a separate-invariance mean-reference-energy profile.

Finite quantum examples retain the logical reference and a discarded encoder
ancilla. The residual estimates use first moments; no reference variance bound
or twirl of a coherent competing input is substituted for the all-code proof.
"""
from __future__ import annotations

from functools import lru_cache
from math import ceil, comb, e, log, log2, pi, sqrt
import unittest

import numpy as np

from test_quadratic_detector import odd_prime_at_least
from test_reference_width import (
    entropy, g, invariant_sector_rows, marginal, setup_state, shannon,
)


TOL = 2e-10


def dither_absolute(displacement: float) -> float:
    """Exact E|displacement+U| for U uniform on [-1/2,1/2]."""
    absolute = abs(displacement)
    return absolute if absolute >= .5 else displacement**2+.25


def mean_bound(energy: float, mean_reference: float, a: float, c: float) -> float:
    return log2(2*e*(sqrt(a*(a+c)*energy/c)+(a/c)*mean_reference+.25))


def conditional_quantities(joint: dict[tuple[int, int], float], ratio: float):
    totals = sorted({total for _, total in joint})
    conditional_entropy = conditional_laplace = absolute = dithered = 0.0
    for total in totals:
        pairs = [(j, probability) for (j, t), probability in joint.items() if t == total]
        mass = sum(probability for _, probability in pairs)
        if mass <= 0:
            continue
        probabilities = np.array([probability/mass for _, probability in pairs])
        conditional_entropy += mass*shannon(probabilities)
        moment = sum(probability*dither_absolute(j-ratio*total) for j, probability in pairs)
        absolute += sum(probability*abs(j-ratio*total) for j, probability in pairs)
        dithered += moment
        conditional_laplace += mass*log2(2*e*moment/mass)
    return conditional_entropy, conditional_laplace, absolute, dithered


def classical_joint(input_probabilities, reference_atoms, a, b):
    c = 1-a-b
    joint = {}
    for n, pn in enumerate(input_probabilities):
        for j in range(n+1):
            for collected in range(n-j+1):
                lost = n-j-collected
                base = pn*comb(n, j)*comb(n-j, collected)*a**j*c**collected*b**lost
                for reference_number, pw in reference_atoms:
                    key = (j, collected+reference_number)
                    joint[key] = joint.get(key, 0.0)+base*pw
    return joint


@lru_cache(maxsize=None)
def prime_for_dimension(d):
    return odd_prime_at_least(d)


class ReferenceMeanTests(unittest.TestCase):
    def test_coherent_encoded_inputs_with_full_invariant_measurement(self):
        for seed, a, b, width, offset in ((12, .3, .1, 3, 1),
                                        (49, .7, .1, 4, 0),
                                        (77, .2, .05, 3, 2),
                                        (18, .4, 0., 4, 1)):
            with self.subTest(seed=seed, a=a, b=b):
                c = 1-a-b
                pure, signal, reference, rng = setup_state(seed, a, b, c, width, offset)
                self.assertGreater(np.linalg.norm(signal-np.diag(np.diag(signal))), .02)
                self.assertGreater(np.linalg.norm(reference-np.diag(np.diag(reference))), .02)
                np.testing.assert_allclose(marginal(pure, (0,)), np.eye(2)/2, atol=TOL)
                rows = invariant_sector_rows(pure.shape[4], pure.shape[6], rng)
                coarse_b = [np.zeros((3, 3), complex) for _ in range(2)]
                coarse_rb = [np.zeros((6, 6), complex) for _ in range(2)]
                joint = {}
                fine_ic = 0.0
                for total, label, row in rows:
                    branch = np.einsum('rfbzdgw,dw->rfbzg', pure, row.conj())
                    receiver = marginal(branch, (2,))
                    logical_receiver = marginal(branch, (0, 2))
                    coarse_b[label % 2] += receiver
                    coarse_rb[label % 2] += logical_receiver
                    fine_ic += entropy(receiver)-entropy(logical_receiver)
                    for j, probability in enumerate(np.diag(receiver).real):
                        joint[j, total] = joint.get((j, total), 0.0)+float(probability)
                coarse_ic = sum(entropy(rb)-entropy(rrb) for rb, rrb in zip(coarse_b, coarse_rb))
                self.assertLessEqual(coarse_ic, fine_ic+TOL)
                signal_numbers = np.diag(signal).real
                reference_numbers = np.diag(reference).real
                expected = classical_joint(signal_numbers, list(enumerate(reference_numbers)), a, b)
                for key in set(joint) | set(expected):
                    self.assertAlmostEqual(joint.get(key, 0), expected.get(key, 0), delta=TOL)
                energy = float(signal_numbers @ np.arange(len(signal_numbers)))
                resource = float(reference_numbers @ np.arange(len(reference_numbers)))
                hc, laplace, absolute, dithered = conditional_quantities(joint, a/c)
                residual = sqrt(a*(a+c)*energy/c)+(a/c)*resource
                self.assertLessEqual(fine_ic, hc+TOL)
                self.assertLessEqual(hc, laplace+TOL)
                self.assertLessEqual(laplace, log2(2*e*dithered)+TOL)
                self.assertLessEqual(absolute, residual+TOL)
                self.assertLessEqual(dithered, absolute+.25+TOL)
                self.assertLessEqual(coarse_ic, mean_bound(energy, resource, a, c)+TOL)

    def test_exact_uniform_dither_without_rounding_estimator(self):
        # The quadrature checks the first-moment formula on both sides of
        # its breakpoint, including fractional aT/c estimator positions.
        centers = np.array([-3.75, -.75, -.5, -.37, -.01, 0., .23, .5, 1.125])
        midpoint_grid = (np.arange(20000)+.5)/20000-.5
        for center in centers:
            with self.subTest(center=center):
                numerical = float(np.mean(abs(center+midpoint_grid)))
                self.assertAlmostEqual(numerical, dither_absolute(float(center)), delta=2e-9)

    def test_sparse_distant_reference_levels_do_not_evade_mean_bound(self):
        a, b = .35, .05
        c = 1-a-b
        input_probabilities = np.array([.1, .2, .3, .4])
        energy = float(input_probabilities @ np.arange(4))
        fixed_bound = mean_bound(energy, 1., a, c)
        old_bounds, entropies = [], []
        for distant in (10, 1000, 10**6, 10**12):
            with self.subTest(distant=distant):
                atoms = [(0, 1-1/distant), (distant, 1/distant)]
                resource = sum(number*probability for number, probability in atoms)
                variance = sum(probability*(number-resource)**2 for number, probability in atoms)
                self.assertEqual(resource, 1)
                self.assertAlmostEqual(variance/(distant-1), 1, delta=1e-12)
                joint = classical_joint(input_probabilities, atoms, a, b)
                hc, laplace, absolute, dithered = conditional_quantities(joint, a/c)
                self.assertAlmostEqual(sum(joint.values()), 1, delta=TOL)
                self.assertLessEqual(hc, laplace+TOL)
                self.assertLessEqual(log2(2*e*dithered), fixed_bound+TOL)
                self.assertLessEqual(absolute, sqrt(a*(a+c)*energy/c)+a/c+TOL)
                old_bounds.append(.5*log2(2*pi*e*(a*(a+c)*energy/c+(a/c)**2*variance+1/12)))
                entropies.append(hc)
        # Separated rare levels do not change the conditional counting
        # entropy here, while the earlier variance-only certificate diverges.
        np.testing.assert_allclose(entropies, entropies[0], atol=TOL)
        self.assertGreater(old_bounds[-1]-old_bounds[0], 15)
        self.assertLess(fixed_bound, old_bounds[-1]-10)

    def test_average_resource_jensen_with_nonuniform_allocations(self):
        allocations = (([0., .01, 1., 100.], [1000., 0., 3., 0.]),
                       ([0., 0., 0., 1e8], [0., 0., 1e6, 0.]),
                       ([0., 0., 0., 0.], [0., 0., 0., 0.]),
                       ([1., 1., 1., 1.], [0., 1., 10., 100.]))
        for a in (.15, .5, .9):
            c = 1-a
            for energies, resources in allocations:
                with self.subTest(a=a, energies=energies, resources=resources):
                    average_single = np.mean([mean_bound(x, m, a, c) for x, m in zip(energies, resources)])
                    combined = mean_bound(float(np.mean(energies)), float(np.mean(resources)), a, c)
                    self.assertLessEqual(average_single, combined+TOL)
                    moments = np.sqrt(a*(a+c)*np.array(energies)/c)+(a/c)*np.array(resources)+.25
                    self.assertLessEqual(average_single, log2(2*e*float(np.mean(moments)))+TOL)

    def test_direct_sizing_and_uniform_profile_for_all_mean_budgets(self):
        nonvacuous = 0
        resource_budgets = (0., .001, .1, 1., 5., 11.99, 12., 13., 32., 128., 1e4, 1e8, 1e12)
        penalty = g(3*pi*pi/64)
        for a in (.2, .49, .8):
            lower_constant = 4+log2(13/a)+penalty
            counting_constant = 2+.5*log2(e)-log2(4/pi)+.5*log2(1/a)
            self.assertGreater(lower_constant, counting_constant)
            c_min = (1-a)/2
            coefficient_a = a*(a+c_min)/c_min
            coefficient_r = a/c_min
            upper_constant = max(log2(e*(1+a)),
                                 log2(2*e*(sqrt(coefficient_a)+coefficient_r+.25)))
            for energy in (1., 1.1, 4., 32., 1e4, 1e8):
                b = min(.25*min(a, 1-a), .5/energy)
                c = 1-a-b
                mu_count = a*energy/(1+c*energy)
                counting = (.5*log2((1+c*energy)*mu_count*(1+mu_count))
                            +log2(4/pi)-.5*log2(e)-g(b*energy))
                self.assertGreaterEqual(counting, .5*log2(energy)-counting_constant-TOL)
                for resource in resource_budgets:
                    with self.subTest(a=a, energy=energy, resource=resource):
                        profile = min(log2(energy), max(.5*log2(energy), log2(resource+1)))
                        collective = g(a*energy)-g(b*energy)
                        upper = min(collective, mean_bound(energy, resource, a, c))
                        self.assertLessEqual(upper, profile+upper_constant+TOL)
                        lower = max(0., counting)
                        if resource >= 12:
                            scale = min(energy, resource/12)
                            dimension = ceil(scale)+1
                            q = prime_for_dimension(dimension)
                            width = 4*dimension
                            stock = q-1+(width-1)/2
                            self.assertLess(q, 2*dimension)
                            self.assertLess(stock, 4*dimension)
                            self.assertLessEqual(4*dimension, 12*scale+TOL)
                            self.assertLess(stock, resource)
                            tail = np.exp(-dimension*np.log1p(1/scale))
                            self.assertLess(tail, .5)
                            signal_mean = scale-dimension*tail/(1-tail)
                            self.assertGreaterEqual(signal_mean, 0)
                            self.assertLess(signal_mean, scale)
                            self.assertLessEqual(signal_mean, energy)
                            ratio = (dimension-1)/(width+1)
                            self.assertLess(ratio, .25)
                            reference_penalty = g(pi*pi*(2*ratio+ratio*ratio)/12)
                            self.assertLess(reference_penalty, penalty)
                            collision = (1/(1+2*a*scale)+1/(1+2*(1-b)*scale))/(1-tail)**2
                            coherent = -log2(collision)-g(b*scale)-reference_penalty
                            target_branch = min(log2(energy), log2(resource+1))-lower_constant
                            self.assertGreaterEqual(coherent, target_branch-TOL)
                            self.assertLessEqual(coherent, upper+TOL)
                            lower = max(lower, coherent)
                        else:
                            self.assertLessEqual(min(log2(energy), log2(resource+1)), log2(13))
                        self.assertGreaterEqual(lower, profile-lower_constant-TOL)
                        self.assertLessEqual(lower, upper+TOL)
                        if profile-lower_constant > 1:
                            nonvacuous += 1
        self.assertGreater(nonvacuous, 30)


if __name__ == '__main__':
    unittest.main()
