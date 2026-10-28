"""Finite resource/continuity checks; not a proof of an asymptotic coding claim.

The robustness checks retain a purifying reference and form the actual receiver
channel. A noisy/coarsened detector's inaccessible optical mode alone is not
treated as its complementary channel.
"""
from __future__ import annotations

import math
import unittest

import numpy as np

import verify
from test_quadratic_detector import odd_prime_at_least


TOL = 4e-10


def thermal_cutoff(energy: float, d: int) -> tuple[np.ndarray, float]:
    ratio = energy / (1 + energy)
    p = ratio ** np.arange(d)
    return p / p.sum(), ratio**d


def cutoff_penalty(tail: float) -> float:
    return -2 * math.log1p(-tail) / math.log(2)


def winter_bound(epsilon: float, d: int) -> float:
    if not 0 <= epsilon <= 1:
        raise ValueError("Half trace distance must lie in [0,1].")
    mixing = (0.0 if epsilon == 0 else
              ((1 + epsilon) * math.log1p(epsilon)
               - epsilon * math.log(epsilon)) / math.log(2))
    return 2 * epsilon * math.log2(d) + mixing


def original_bound(energy: float, a: float, b: float) -> tuple[float, float]:
    collision = 1 / (1 + 2 * a * energy) + 1 / (1 + 2 * (1 - b) * energy)
    return -math.log2(collision) - verify.g(b * energy), collision


def purified_split(p: np.ndarray, a: float, b: float, helper_size: int) -> np.ndarray:
    """Return amplitudes indexed R, B, Z, D, with a padded helper space."""
    d = len(p)
    v = verify.splitter(d, a, b).reshape(d, d, d, d)
    psi = np.zeros((d, d, d, helper_size), complex)
    psi[:, :, :, :d] = np.einsum('n,bzkn->nbzk', np.sqrt(p), v)
    return psi


def detector_unitary(q: int, s: int, helper_size: int,
                     linear_offset: float = 0.0,
                     quadratic_offset: float = 0.0,
                     fourier_rotation: float = 0.0) -> tuple[np.ndarray, np.ndarray]:
    """Return U and its Fourier factor; optional rotations cause leakage."""
    k = np.arange(q)
    fourier = np.eye(helper_size, dtype=complex)
    fourier[:q, :q] = np.exp(-2j * np.pi * np.outer(k, k) / q) / math.sqrt(q)
    if fourier_rotation:
        rotation = np.eye(helper_size, dtype=complex)
        for inside, outside, angle in ((0, q, fourier_rotation),
                                       (1, q + 1, .7 * fourier_rotation)):
            co, si = math.cos(angle), math.sin(angle)
            rotation[np.ix_((inside, outside), (inside, outside))] = ((co, si), (-si, co))
        fourier = rotation @ fourier
    diagonal = np.ones(helper_size, complex)
    diagonal[:q] = np.exp(-1j * (linear_offset * k
                               + (2 * np.pi * s / q + quadratic_offset) * k**2))
    return fourier @ np.diag(diagonal), fourier


def flagged_states(psi: np.ndarray, unitary: np.ndarray, q: int,
                   erase_probability: float = 0.0):
    """Trace Z and measured D to form RBX, retaining the coarse outside flag.

    Z blocks are returned only to demonstrate that S(B|X)-S(Z|X) can fail
    once the fine detector record is lost. They are not used for the rate.
    """
    out = np.einsum('ok,rbzk->rbzo', unitary, psi)
    d = psi.shape[0]
    rb_blocks, z_blocks = [], []
    for indices in [np.array([k]) for k in range(q)] + [np.arange(q, out.shape[3])]:
        part = out[:, :, :, indices]
        rb = np.einsum('rbzk,uvzk->rbuv', part, part.conj()).reshape(d*d, d*d)
        zz = np.einsum('rbzk,rbwk->zw', part, part.conj())
        rb_blocks.append(rb)
        z_blocks.append(zz)
    rb_blocks, z_blocks = np.array(rb_blocks), np.array(z_blocks)
    if erase_probability:
        # A classical erasure of the fine outcome: the lost record belongs
        # to the environment, even though the receiver keeps the erasure flag.
        for blocks in (rb_blocks, z_blocks):
            total = blocks.sum(axis=0)
            blocks *= 1 - erase_probability
            blocks[q] += erase_probability * total
    return rb_blocks, z_blocks, out


def b_blocks(rb_blocks: np.ndarray, d: int) -> np.ndarray:
    return np.einsum('yrbrv->ybv', rb_blocks.reshape(-1, d, d, d, d))


def coherent_information(rb_blocks: np.ndarray, d: int) -> float:
    # For each subnormalized flag block, its normalization entropy cancels.
    return sum(verify.von_neumann(bb) - verify.von_neumann(rb)
               for bb, rb in zip(b_blocks(rb_blocks, d), rb_blocks))


def cq_distance(left: np.ndarray, right: np.ndarray) -> float:
    return sum(float(np.abs(np.linalg.eigvalsh(x - y)).sum())
               for x, y in zip(left, right)) / 2


def select_setting(psi: np.ndarray, q: int):
    d, helper_size = psi.shape[0], psi.shape[3]
    candidates = []
    for s in range(q):
        unitary, fourier = detector_unitary(q, s, helper_size)
        rb, zz, out = flagged_states(psi, unitary, q)
        average_purity = 0.0
        for bb in b_blocks(rb, d):
            probability = float(np.trace(bb).real)
            if probability > 1e-14:
                average_purity += float(np.trace(bb @ bb).real) / probability
        candidates.append((average_purity, s, unitary, fourier, rb, zz, out))
    return min(candidates, key=lambda item: item[0])


class DetectorResourceChecks(unittest.TestCase):
    def assert_close(self, left, right, atol=TOL):
        np.testing.assert_allclose(left, right, atol=atol, rtol=0)

    def test_explicit_cutoff_and_positive_finite_rate(self):
        cases = ((5, 1., .7, 0.), (6, 1., .8, .01), (8, 2., .65, .05))
        for d, energy, a, b in cases:
            with self.subTest(d=d, energy=energy, a=a, b=b):
                q = odd_prime_at_least(d)
                p, tail = thermal_cutoff(energy, d)
                mean = float(p @ np.arange(d))
                self.assert_close(mean, energy - d * tail / (1 - tail))
                self.assertLess(mean, energy)
                bd, zd = verify.marginals(verify.splitter(d, a, b), np.diag(p))
                bm = np.einsum('bkBk->bB', bd.reshape(d, d, d, d))
                zm = np.einsum('zkZk->zZ', zd.reshape(d, d, d, d))
                pb = float(np.trace(bm @ bm).real)
                pbd = float(np.trace(bd @ bd).real)
                # Separate checks prevent an error in one marginal cancelling
                # an error in the other in the claimed collision bound.
                self.assertLessEqual((1-tail)**2 * pb, 1/(1+2*a*energy) + TOL)
                self.assertLessEqual((1-tail)**2 * pbd, 1/(1+2*(1-b)*energy) + TOL)
                self.assertLessEqual(verify.von_neumann(zm), verify.g(b*energy) + TOL)
                rate, collision = original_bound(energy, a, b)
                finite_bound = -math.log2(pb+pbd) - verify.von_neumann(zm)
                explicit_bound = rate - cutoff_penalty(tail)
                self.assertLessEqual(pb+pbd, collision/(1-tail)**2 + TOL)
                self.assertGreaterEqual(finite_bound + TOL, explicit_bound)
                self.assertGreater(explicit_bound, .1)
                psi = purified_split(p, a, b, q+2)
                before_distribution = np.sum(abs(psi)**2, axis=(0, 1, 2))
                self.assert_close(before_distribution @ np.arange(q+2), (1-a-b)*mean)
                _, _, _, _, rb, zz, out = select_setting(psi, q)
                self.assert_close(np.vdot(psi, psi), 1)
                self.assertGreaterEqual(coherent_information(rb, d) + TOL, finite_bound)
                # The original rank-one fine record permits B-minus-Z; the
                # robustness test below deliberately leaves that setting.
                naive = sum(verify.von_neumann(bb)-verify.von_neumann(z)
                            for bb, z in zip(b_blocks(rb, d), zz))
                self.assert_close(coherent_information(rb, d), naive)
                distribution = np.sum(abs(out)**2, axis=(0, 1, 2))
                self.assert_close(distribution[:q], np.full(q, 1/q))
                self.assert_close(distribution[q:], 0)
                self.assert_close(distribution @ np.arange(q+2), (q-1)/2)
                self.assertGreaterEqual((q-1)/2-(1-a-b)*mean, -TOL)

    def test_dimension_choice_meets_requested_tail_penalty(self):
        for energy in (.01, .1, 1., 10., 1000.):
            for tolerance in (1., .1, .01, .0001):
                with self.subTest(energy=energy, tolerance=tolerance):
                    tail_target = -math.expm1(-tolerance*math.log(2)/2)
                    d = max(2, math.ceil(math.log(1/tail_target)/math.log1p(1/energy)))
                    tail = math.exp(-d*math.log1p(1/energy))
                    self.assertLessEqual(tail, tail_target*(1+1e-12))
                    self.assertLessEqual(cutoff_penalty(tail), tolerance+TOL)
        for d in (2, 3, 8, 100, 10**6):
            for budget in (1., .1, .001):
                with self.subTest(d=d, implementation_budget=budget):
                    epsilon = budget/(4*math.log2(8*d/budget))
                    self.assertLessEqual(winter_bound(epsilon, d), budget)

    def test_implementation_error_with_reference_and_lost_record(self):
        cases = ((5, 1., .7, 0.), (6, 1., .8, .01), (8, 2., .65, .05))
        for d, energy, a, b in cases:
            with self.subTest(d=d, a=a, b=b):
                q = odd_prime_at_least(d)
                p, tail = thermal_cutoff(energy, d)
                psi = purified_split(p, a, b, q+2)
                _, s, ideal, ideal_fourier, rb_ideal, _, out_ideal = select_setting(psi, q)
                m = d-1
                delta_linear, delta_quadratic = .001/m, .001/(m*m)
                actual, actual_fourier = detector_unitary(
                    q, s, q+2, delta_linear, delta_quadratic, .004)
                eta_fourier = float(np.linalg.norm((actual_fourier-ideal_fourier)[:, :q], 2))
                eta_unitary = float(np.linalg.norm((actual-ideal)[:, :d], 2))
                coefficient_bound = eta_fourier + m*abs(delta_linear) + m*m*abs(delta_quadratic)
                self.assertLessEqual(eta_unitary, coefficient_bound+TOL)
                rb_actual_fine, _, out_actual = flagged_states(psi, actual, q)
                before_measurement = math.sqrt(max(0., 1-abs(np.vdot(out_ideal, out_actual))**2))
                measured_distance = cq_distance(rb_ideal, rb_actual_fine)
                self.assertLessEqual(before_measurement, eta_unitary+TOL)
                self.assertLessEqual(measured_distance, before_measurement+TOL)
                # There are two leaked output levels grouped into one flag.
                self.assertGreater(float(np.trace(rb_actual_fine[-1]).real), 1e-7)
                erasure = .005
                rb_actual, z_actual, _ = flagged_states(psi, actual, q, erasure)
                epsilon = cq_distance(rb_ideal, rb_actual)
                epsilon_budget = min(1., coefficient_bound+erasure)
                self.assertLessEqual(epsilon, measured_distance+erasure+TOL)
                self.assertLessEqual(epsilon, epsilon_budget+TOL)
                self.assertGreater(epsilon, .001)
                self.assert_close(sum(np.trace(x) for x in rb_actual), 1)
                # A channel on A must retain the original reference marginal.
                actual_r = np.einsum('yrbub->ru', rb_actual.reshape(-1, d, d, d, d))
                self.assert_close(actual_r, np.diag(p))
                ideal_ic = coherent_information(rb_ideal, d)
                actual_ic = coherent_information(rb_actual, d)
                self.assertLessEqual(abs(actual_ic-ideal_ic), winter_bound(epsilon, d)+TOL)
                rate, _ = original_bound(energy, a, b)
                guaranteed = rate-cutoff_penalty(tail)-winter_bound(epsilon_budget, d)
                self.assertGreater(guaranteed, .1)
                self.assertGreaterEqual(actual_ic+TOL, guaranteed)
                # Discarding the fine record leaves an unresolved complement.
                # Its omission produces a demonstrably wrong entropy formula.
                naive = sum(verify.von_neumann(bb)-verify.von_neumann(zz)
                            for bb, zz in zip(b_blocks(rb_actual, d), z_actual))
                self.assertGreater(naive-actual_ic, .001)


if __name__ == '__main__':
    unittest.main()
