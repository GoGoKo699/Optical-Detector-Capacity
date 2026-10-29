"""Finite checks of an energy-conserving detector with a sine reference.

The sector lift and sine battery are established constructions; see Aberg,
Phys. Rev. Lett. 113, 150402 (2014), and Chiribella, Yang, and Renner,
Phys. Rev. X 11, 021014 (2021). These tests do not certify hardware efficiency,
optimal reference energy, restoration, or repeated use of the same reference.
"""
from __future__ import annotations

import math
import unittest

import numpy as np

import verify
from test_detector_resources import (
    b_blocks, coherent_information, cq_distance, cutoff_penalty,
    original_bound, purified_split, select_setting, thermal_cutoff, winter_bound,
)
from test_quadratic_detector import odd_prime_at_least


TOL = 5e-10


def sine_reference(q: int, length: int) -> np.ndarray:
    """Initial support starts at q-1; leave a top buffer of q-1 levels."""
    h = q-1
    reference = np.zeros(length+2*h, complex)
    levels = np.arange(1, length+1)
    reference[h:h+length] = math.sqrt(2/(length+1))*np.sin(math.pi*levels/(length+1))
    return reference


def apply_conserving_lift(amplitudes: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    """Apply actual q-by-q U blocks in complete total-number sectors.

    Last axes are D,W. For total N<q-1 or N>W_max use the identity; otherwise
    {|j,N-j>:0<=j<q} is a complete q-dimensional block. No cyclic shift is
    used at either end of the finite reference ladder.
    """
    q, wdim = amplitudes.shape[-2:]
    if unitary.shape != (q, q):
        raise ValueError("Unitary and detector dimensions do not match.")
    output = amplitudes.copy()
    j = np.arange(q)
    for total in range(q-1, wdim):
        output[..., j, total-j] = np.einsum(
            'jk,...k->...j', unitary, amplitudes[..., j, total-j])
    return output


def lifted_isometry(unitary: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Return amplitudes W[j,w,k] from the finite-sector joint unitary."""
    q = len(unitary)
    basis = np.zeros((q, q, len(reference)), complex)
    for k in range(q):
        basis[k, k, :] = reference
    return apply_conserving_lift(basis, unitary).transpose(1, 2, 0)


def reduced_matrix(amplitudes: np.ndarray) -> np.ndarray:
    """Keep all axes except the last, which is the discarded reference."""
    matrix = amplitudes.reshape(-1, amplitudes.shape[-1])
    return matrix @ matrix.conj().T


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.abs(np.linalg.eigvalsh(left-right)).sum())/2


def reference_bounds(q: int, length: int) -> tuple[float, float]:
    delta = 2*math.sin(math.pi/(2*(length+1)))
    # The first is a joint/Stinespring norm bound. The second is a
    # half-diamond bound only after discarding the reference.
    joint = (q-1)*delta
    reduced = min(1., math.pi**2*(q-1)**2*delta**2/4)
    return joint, reduced


def phase_quadrature(unitary: np.ndarray, reference: np.ndarray, length: int):
    """Exact trapezoidal quadrature for this finite trigonometric polynomial."""
    q = len(unitary)
    points = 2*(length+2*q)+1
    angles = -math.pi+2*math.pi*np.arange(points)/points
    amplitudes = np.exp(1j*np.outer(angles, np.arange(len(reference)))) @ reference
    weights = abs(amplitudes)**2/points
    k = np.arange(q)
    rotated = [np.exp(-1j*k*angle)[:, None]*unitary*np.exp(1j*k*angle)[None, :]
               for angle in angles]
    return angles, weights, rotated


def random_unitary(q: int, rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(q, q))+1j*rng.normal(size=(q, q))
    unitary, diagonal = np.linalg.qr(matrix)
    phases = np.diag(diagonal)
    return unitary @ np.diag(phases.conj()/abs(phases))


class FiniteReferenceChecks(unittest.TestCase):
    def assert_close(self, left, right, atol=TOL):
        np.testing.assert_allclose(left, right, atol=atol, rtol=0)

    def test_actual_sector_unitary_and_both_ladder_boundaries(self):
        rng = np.random.default_rng(2026102901)
        for q, length in ((3, 4), (5, 7)):
            with self.subTest(q=q, length=length):
                unitary = random_unitary(q, rng)
                reference = sine_reference(q, length)
                wdim = len(reference)
                # Apply the actual sector construction to every basis vector,
                # including sectors never occupied by the prepared reference.
                columns = np.eye(q*wdim, dtype=complex).reshape(q*wdim, q, wdim)
                joint = apply_conserving_lift(columns, unitary).reshape(q*wdim, q*wdim).T
                self.assert_close(joint.conj().T @ joint, np.eye(q*wdim))
                total_numbers = (np.arange(q)[:, None]+np.arange(wdim)[None, :]).ravel()
                self.assert_close((total_numbers[:, None]-total_numbers[None, :])*joint, 0)
                for k in range(q):
                    for w in range(wdim):
                        total = k+w
                        if total < q-1 or total >= wdim:
                            self.assert_close(joint[:, k*wdim+w], np.eye(q*wdim)[:, k*wdim+w])
                # High occupation inputs stay in valid sectors. Their shifted
                # reference indices reach neither a negative index nor wrap.
                stinespring = lifted_isometry(unitary, reference)
                explicit = np.zeros_like(stinespring)
                for k in range(q):
                    for j in range(q):
                        for n in range(q-1, q-1+length):
                            shifted = n+k-j
                            self.assertGreaterEqual(shifted, 0)
                            self.assertLess(shifted, wdim)
                            explicit[j, shifted, k] += unitary[j, k]*reference[n]
                self.assert_close(stinespring, explicit)
                self.assert_close(stinespring.reshape(q*wdim, q).conj().T
                                  @ stinespring.reshape(q*wdim, q), np.eye(q))

    def test_sine_moments_phase_integral_and_entangled_channel_error(self):
        rng = np.random.default_rng(2026102902)
        for q, length in ((3, 20), (5, 36), (7, 52)):
            with self.subTest(q=q, length=length):
                unitary = random_unitary(q, rng)
                reference = sine_reference(q, length)
                self.assert_close(np.vdot(reference, reference), 1)
                self.assert_close(abs(reference)**2 @ np.arange(len(reference)),
                                  q-1+(length-1)/2)
                neighbor = np.vdot(reference[1:], reference[:-1]).real
                self.assert_close(neighbor, math.cos(math.pi/(length+1)))
                stinespring = lifted_isometry(unitary, reference)
                ideal_isometry = np.einsum('jk,w->jwk', unitary, reference)
                joint_bound, channel_bound = reference_bounds(q, length)
                self.assertLessEqual(np.linalg.norm(
                    (stinespring-ideal_isometry).reshape(-1, q), 2), joint_bound+TOL)
                # Choi equality verifies the complete reduced channel, not
                # just its action on diagonal detector states.
                choi_amplitudes = stinespring.transpose(2, 0, 1)/math.sqrt(q)
                actual_choi = reduced_matrix(choi_amplitudes)
                angles, weights, rotations = phase_quadrature(unitary, reference, length)
                self.assert_close(weights.sum(), 1)
                self.assert_close(np.sum(weights*np.sin(angles)), 0)
                self.assert_close(np.sum(weights*4*np.sin(angles/2)**2), 2*(1-neighbor))
                mixture_choi = np.zeros((q*q, q*q), complex)
                for weight, rotated in zip(weights, rotations):
                    vec = rotated.T.reshape(-1)/math.sqrt(q)
                    mixture_choi += weight*np.outer(vec, vec.conj())
                self.assert_close(actual_choi, mixture_choi)
                ideal_vec = unitary.T.reshape(-1)/math.sqrt(q)
                self.assertLessEqual(trace_distance(actual_choi, np.outer(ideal_vec, ideal_vec.conj())),
                                     channel_bound+TOL)
                # Several full-Schmidt-rank entangled inputs additionally
                # check the operational error and exact energy conservation.
                for _ in range(3):
                    psi = rng.normal(size=(q, q))+1j*rng.normal(size=(q, q))
                    psi /= np.linalg.norm(psi)
                    actual = np.einsum('jwk,rk->rjw', stinespring, psi)
                    ideal = np.einsum('jk,rk->rj', unitary, psi).reshape(-1)
                    self.assertLessEqual(trace_distance(reduced_matrix(actual),
                                                       np.outer(ideal, ideal.conj())), channel_bound+TOL)
                    incoming = np.sum(abs(psi)**2*np.arange(q)[None, :])
                    incoming += abs(reference)**2 @ np.arange(len(reference))
                    outgoing = np.sum(abs(actual)**2*(np.arange(q)[None, :, None]
                                                     + np.arange(len(reference))[None, None, :]))
                    self.assert_close(incoming, outgoing)
                    # Tracing D does not generally restore the pure reference.
                    ref_matrix = actual.reshape(q*q, -1).T
                    ref_matrix = ref_matrix @ ref_matrix.conj().T
                    self.assertLess(float(np.trace(ref_matrix @ ref_matrix).real), .99999)

    def test_actual_optical_receiver_includes_discarded_reference(self):
        for d, energy, a, b in ((5, 1., .7, 0.), (6, 1., .8, .01)):
            with self.subTest(d=d, a=a, b=b):
                q = odd_prime_at_least(d)
                p, tail = thermal_cutoff(energy, d)
                psi = purified_split(p, a, b, q)
                _, _, unitary, _, rb_ideal, _, _ = select_setting(psi, q)
                target_error = .005
                length = math.ceil(math.pi**2*(q-1)/(2*math.sqrt(target_error)))
                reference = sine_reference(q, length)
                _, error_bound = reference_bounds(q, length)
                self.assertLessEqual(error_bound, target_error)
                # Fresh independent W per channel use yields a memoryless
                # detector. Here the actual state retains R,B,Z,D,W until
                # the physical number measurement and traces are performed.
                before = np.einsum('rbzk,w->rbzkw', psi, reference)
                actual = apply_conserving_lift(before, unitary)
                rb_actual = np.einsum('rbzjw,uvzjw->jrbuv', actual, actual.conj())
                rb_actual = rb_actual.reshape(q, d*d, d*d)
                rb_actual = np.concatenate((rb_actual, np.zeros((1, d*d, d*d))), axis=0)
                self.assert_close(sum(np.trace(x) for x in rb_actual), 1)
                self.assert_close(np.einsum('yrbub->ru', rb_actual.reshape(-1, d, d, d, d)), np.diag(p))
                error = cq_distance(rb_actual, rb_ideal)
                self.assertLessEqual(error, error_bound+TOL)
                ideal_ic = coherent_information(rb_ideal, d)
                actual_ic = coherent_information(rb_actual, d)
                self.assertLessEqual(abs(actual_ic-ideal_ic), winter_bound(error, d)+TOL)
                rate, _ = original_bound(energy, a, b)
                guarantee = rate-cutoff_penalty(tail)-winter_bound(error_bound, d)
                self.assertGreater(guarantee, .2)
                self.assertGreaterEqual(actual_ic+TOL, guarantee)
                # Finite reference still gives a uniform number distribution
                # for a diagonal helper input and a flat-modulus Fourier U.
                number_probabilities = np.array([np.trace(bb).real for bb in b_blocks(rb_actual, d)])
                self.assert_close(number_probabilities[:q], np.full(q, 1/q))
                detector_mean = number_probabilities[:q] @ np.arange(q)
                self.assert_close(detector_mean, (q-1)/2)
                reference_probabilities = np.sum(abs(actual)**2, axis=(0, 1, 2, 3))
                final_reference_mean = reference_probabilities @ np.arange(len(reference))
                initial_reference_mean = q-1+(length-1)/2
                collected_mean = (1-a-b)*float(p @ np.arange(d))
                self.assert_close(final_reference_mean,
                                  initial_reference_mean+collected_mean-detector_mean)


if __name__ == '__main__':
    unittest.main()
