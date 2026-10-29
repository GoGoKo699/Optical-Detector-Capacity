"""Checks of the direct entropy bound for a fresh finite sine reference.

The selected quadratic setting is selected using the IDEAL detector's receiver
purity. It is not reoptimized after introducing the finite reference. All actual
rates below come from the purified receiver-reference state, so the discarded
phase reference remains part of the complementary system.
"""
from __future__ import annotations

import math
import unittest

import numpy as np

import verify
from test_detector_resources import (
    b_blocks, coherent_information, cutoff_penalty, original_bound,
    purified_split, select_setting, thermal_cutoff, winter_bound,
)
from test_finite_reference import (
    apply_conserving_lift, reference_bounds, sine_reference,
)
from test_quadratic_detector import odd_prime_at_least


TOL = 8e-10


def shifted(reference: np.ndarray, displacement: int) -> np.ndarray:
    """A noncyclic shift; test inputs have sufficient physical boundary guards."""
    output = np.zeros_like(reference)
    if displacement > 0:
        output[displacement:] = reference[:-displacement]
    elif displacement < 0:
        output[:displacement] = reference[-displacement:]
    else:
        output[:] = reference
    return output


def conditional_reference_mean_bound(d: int, length: int) -> float:
    ratio = (d-1)/(length+1)
    return math.pi**2*(2*ratio+ratio*ratio)/12


class DirectReferenceChecks(unittest.TestCase):
    def assert_close(self, left, right, atol=TOL):
        np.testing.assert_allclose(left, right, atol=atol, rtol=0)

    def test_full_optical_channel_with_ideal_selected_setting(self):
        # These are finite instances with a positive direct guarantee. The
        # previous uniform-gate continuity certificate is much weaker here;
        # that comparison makes no claim that the actual channel has failed.
        cases = ((8, 2., .85, .01, 6),
                 (9, 3., .8, .01, 10),
                 (7, 2., .9, 0., 10))
        for d, energy, a, b, width_factor in cases:
            with self.subTest(d=d, energy=energy, a=a, b=b):
                q = odd_prime_at_least(d)
                h = q-1
                length = width_factor*h
                p, tail = thermal_cutoff(energy, d)
                psi = purified_split(p, a, b, q)
                # Select once, on the ideal channel, exactly as in the proof.
                _, setting, unitary, _, rb_ideal, _, _ = select_setting(psi, q)
                reference = sine_reference(q, length)
                wdim = len(reference)
                # Each invocation starts with the same fresh independent
                # pure reference. No previous output reference is reused.
                incoming = np.einsum('rbzk,w->rbzkw', psi, reference)
                actual = apply_conserving_lift(incoming, unitary)
                rb_actual = np.einsum('rbzjw,uvzjw->jrbuv', actual, actual.conj())
                rb_actual = rb_actual.reshape(q, d*d, d*d)
                rb_actual = np.concatenate((rb_actual, np.zeros((1, d*d, d*d))), axis=0)
                actual_b = b_blocks(rb_actual, d)
                ideal_b = b_blocks(rb_ideal, d)
                probabilities = np.array([np.trace(block).real for block in rb_actual])
                self.assert_close(probabilities[:q], np.full(q, 1/q))
                self.assert_close(probabilities[q], 0)
                self.assert_close(np.einsum('yrbub->ru', rb_actual.reshape(-1, d, d, d, d)),
                                  np.diag(p))

                # In the receiver number basis the finite-reference detector
                # dephases the ideal conditional B state by a positive-definite
                # shift-overlap kernel. Verify the state identity, not only
                # its entropy consequence.
                damping = np.empty((d, d), complex)
                for row in range(d):
                    for column in range(d):
                        damping[row, column] = np.vdot(reference, shifted(reference, row-column))
                self.assert_close(np.diag(damping), 1)
                self.assertGreaterEqual(float(np.linalg.eigvalsh(damping).min()), -TOL)
                for j in range(q):
                    self.assert_close(actual_b[j], damping*ideal_b[j])
                    self.assertGreaterEqual(verify.von_neumann(q*actual_b[j])+TOL,
                                            verify.von_neumann(q*ideal_b[j]))

                collected = verify.thin(p, 1-a-b)
                mu = conditional_reference_mean_bound(d, length)
                entropy_bound = verify.g(mu)
                conditional_entropies = []
                conditional_z_entropies = []
                conditional_w = []
                compressed_spectrum = None
                for j in range(q):
                    # Directly derive W|j by tracing the actual R,B,Z state.
                    part = actual[:, :, :, j, :]
                    matrix = part.reshape(-1, wdim)
                    reference_j = q*(matrix.T @ matrix.conj())
                    conditional_w.append(reference_j)
                    expected = np.zeros((wdim, wdim), complex)
                    for k in range(d):
                        translated = shifted(reference, k-j)
                        self.assert_close(np.vdot(translated, translated), 1)
                        expected += collected[k]*np.outer(translated, translated.conj())
                    self.assert_close(reference_j, expected)

                    # The smaller interval J=K+d-1 is sufficient for W|j.
                    # All flags give translates of the same density matrix.
                    start, support = h-j, length+d-1
                    cropped = reference_j[start:start+support, start:start+support]
                    self.assert_close(np.trace(cropped), 1)
                    spectrum = np.linalg.eigvalsh(cropped)
                    if compressed_spectrum is None:
                        compressed_spectrum = spectrum
                    else:
                        self.assert_close(spectrum, compressed_spectrum)
                    entropy_w = verify.von_neumann(cropped)
                    conditional_entropies.append(entropy_w)
                    self.assertLessEqual(entropy_w, entropy_bound+TOL)
                    # The full conditional complement is ZW. Conditional
                    # purity identifies its entropy with S(RB|j), not S(Z|j).
                    z_j = q*np.einsum('rbzw,rbZw->zZ', part, part.conj())
                    entropy_z = verify.von_neumann(z_j)
                    conditional_z_entropies.append(entropy_z)
                    self.assertLessEqual(verify.von_neumann(q*rb_actual[j]),
                                         entropy_z+entropy_w+TOL)

                self.assert_close(conditional_entropies, conditional_entropies[0])
                bd, zd = verify.marginals(verify.splitter(d, a, b), np.diag(p))
                marginal_b = np.einsum('bkBk->bB', bd.reshape(d, d, d, d))
                marginal_z = np.einsum('zkZk->zZ', zd.reshape(d, d, d, d))
                collision = float(np.trace(marginal_b@marginal_b).real
                                  + np.trace(bd@bd).real)
                self.assertLessEqual(np.mean(conditional_z_entropies),
                                     verify.von_neumann(marginal_z)+TOL)
                ideal_average_b_entropy = sum(verify.von_neumann(q*block)/q
                                              for block in ideal_b[:q])
                self.assertGreaterEqual(ideal_average_b_entropy+TOL, -math.log2(collision))
                direct = -math.log2(collision)-verify.von_neumann(marginal_z)-entropy_bound
                actual_ic = coherent_information(rb_actual, d)
                self.assertGreaterEqual(actual_ic+TOL, direct)
                rate, _ = original_bound(energy, a, b)
                explicit_direct = rate-cutoff_penalty(tail)-entropy_bound
                self.assertGreaterEqual(direct+TOL, explicit_direct)
                self.assertGreater(explicit_direct, .15)
                # Uniform gate approximation followed by dimension-dependent
                # continuity gives a negative certificate in these same cases.
                _, uniform_error = reference_bounds(q, length)
                uniform_certificate = rate-cutoff_penalty(tail)-winter_bound(uniform_error, d)
                self.assertLess(uniform_certificate, 0)
                self.assertGreater(explicit_direct-uniform_certificate, 1)

                # Exact reference accounting includes the consumed/correlated
                # output. No restoration or reset cost is inferred.
                initial_mean = h+(length-1)/2
                self.assert_close(abs(reference)**2 @ np.arange(wdim), initial_mean)
                averaged_w = sum(conditional_w)/q
                final_mean = np.trace(averaged_w*np.arange(wdim)[:, None]).real
                signal_mean = float(p @ np.arange(d))
                self.assert_close(final_mean,
                                  initial_mean+(1-a-b)*signal_mean-h/2)
                self.assertGreater(initial_mean-final_mean, .1)
                self.assertLess(float(np.trace(averaged_w@averaged_w).real), .999)
                self.assertGreaterEqual(setting, 0)
                self.assertLess(setting, q)


if __name__ == '__main__':
    unittest.main()
