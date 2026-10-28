"""Finite checks for quadratic-phase compression; not a coding theorem certificate."""
from __future__ import annotations

import itertools
import math
import unittest

import numpy as np

import verify


def odd_prime_at_least(d: int) -> int:
    q = max(3, d)
    while any(q % p == 0 for p in range(2, math.isqrt(q) + 1)):
        q += 1
    return q


def phase_vector(d: int, q: int, r: int, s: int) -> np.ndarray:
    k = np.arange(d)
    return np.exp(2j * np.pi * ((r * k + s * k * k) % q) / q)


def survives(k: int, l: int, m: int, n: int, q: int) -> bool:
    """Exact character average for conjugate phases at k and m."""
    return ((k + m - l - n) % q == 0
            and (k * k + m * m - l * l - n * n) % q == 0)


def conditional(blocks: np.ndarray, phases: np.ndarray) -> np.ndarray:
    return np.einsum('k,l,jkJl->jJ', phases.conj(), phases, blocks)


def purity(rho: np.ndarray) -> float:
    return float(np.trace(rho @ rho).real)


def collision_identity(bd: np.ndarray, bdim: int, ddim: int) -> float:
    blocks = bd.reshape(bdim, ddim, bdim, ddim)
    bm = np.einsum('jkJk->jJ', blocks)
    return (purity(bm) + purity(bd)
            - sum(purity(blocks[:, k, :, k]) for k in range(ddim)))


class QuadraticPhaseChecks(unittest.TestCase):
    def assert_close(self, left, right, atol: float = 3e-11):
        np.testing.assert_allclose(left, right, atol=atol, rtol=0)

    def test_exact_fourth_moments_and_support_bound(self):
        for d in range(2, 13):
            q = odd_prime_at_least(d)
            with self.subTest(d=d, q=q):
                self.assertLess(q, 2 * d)
                for k, l, m, n in itertools.product(range(d), repeat=4):
                    self.assertEqual(survives(k, l, m, n, q),
                                     sorted((k, m)) == sorted((l, n)))
                # Distinct nontrivial difference characters plus the constant
                # are orthonormal on the q^2-point uniform phase ensemble.
                characters = {(0, 0)}
                for k, l in itertools.permutations(range(d), 2):
                    characters.add(((l - k) % q, (l * l - k * k) % q))
                self.assertEqual(len(characters), d * (d - 1) + 1)
                self.assertLessEqual(len(characters), q * q)

    def test_bad_moduli_have_extra_collisions(self):
        # Characteristic two loses the second equation; arithmetic modulo an
        # odd composite is not arithmetic in a finite field.
        self.assertTrue(survives(0, 1, 0, 1, 2))
        self.assertNotEqual(sorted((0, 0)), sorted((1, 1)))
        self.assertTrue(survives(0, 3, 0, 6, 9))
        self.assertNotEqual(sorted((0, 0)), sorted((3, 6)))

    def test_complete_povms_and_fourier_realization_on_code_support(self):
        for d in (2, 3, 4, 5, 8):
            q = odd_prime_at_least(d)
            k = np.arange(q)
            fourier = np.exp(-2j * np.pi * np.outer(k, k) / q) / math.sqrt(q)
            full_effects = np.zeros((d, d), complex)
            with self.subTest(d=d, q=q):
                self.assert_close(fourier.conj().T @ fourier, np.eye(q))
                for s in range(q):
                    fixed_effects = np.zeros((d, d), complex)
                    diagonal = np.diag(np.exp(-2j * np.pi * s * k * k / q))
                    unitary = fourier @ diagonal
                    for r in range(q):
                        v = phase_vector(d, q, r, s)
                        effect = np.outer(v, v.conj()) / q
                        fixed_effects += effect
                        realized = np.outer(unitary[r, :d].conj(), unitary[r, :d])
                        self.assert_close(realized, effect)
                        full_effects += effect / q
                    self.assert_close(fixed_effects, np.eye(d))
                self.assert_close(full_effects, np.eye(d))

    def test_purity_for_random_mixed_states_with_diagonal_helper_margin(self):
        rng = np.random.default_rng(20261029)
        for bdim, d in ((2, 2), (3, 3), (2, 4), (3, 5)):
            q = odd_prime_at_least(d)
            z = (rng.normal(size=(bdim * d, bdim * d))
                 + 1j * rng.normal(size=(bdim * d, bdim * d)))
            bd = z @ z.conj().T
            bd /= np.trace(bd)
            dm = np.einsum('jkjK->kK', bd.reshape(bdim, d, bdim, d))
            eigenvalues, eigenvectors = np.linalg.eigh(dm)
            invsqrt = ((eigenvectors * eigenvalues**-0.5)
                       @ eigenvectors.conj().T)
            desired = rng.dirichlet(np.ones(d))
            transform = np.kron(np.eye(bdim), np.diag(np.sqrt(desired)) @ invsqrt)
            bd = transform @ bd @ transform.conj().T
            blocks = bd.reshape(bdim, d, bdim, d)
            with self.subTest(bdim=bdim, d=d):
                self.assert_close(np.einsum('jkjK->kK', blocks), np.diag(desired))
                measured = []
                for r, s in itertools.product(range(q), repeat=2):
                    sb = conditional(blocks, phase_vector(d, q, r, s))
                    self.assert_close(np.trace(sb), 1)
                    measured.append(purity(sb))
                self.assert_close(np.mean(measured), collision_identity(bd, bdim, d))

    def test_optical_information_bound_and_fixed_setting_selection(self):
        for d, a, b, energy in ((2, .25, 0., 2.),
                               (3, .25, .1, 2.),
                               (4, .7, .1, 10.),
                               (5, .25, .01, 4.),
                               (8, .4, .03, 5.)):
            q = odd_prime_at_least(d)
            thermal = (energy / (1 + energy))**np.arange(d)
            thermal /= thermal.sum()
            bd, zd = verify.marginals(verify.splitter(d, a, b), np.diag(thermal))
            bb = bd.reshape(d, d, d, d)
            zz = zd.reshape(d, d, d, d)
            bm = np.einsum('jkJk->jJ', bb)
            zm = np.einsum('jkJk->jJ', zz)
            collision_upper = purity(bm) + purity(bd)
            bound = -math.log2(collision_upper) - verify.von_neumann(zm)
            purities, infos = [], []
            for s in range(q):
                per_setting_purity, per_setting_info = [], []
                for r in range(q):
                    phases = phase_vector(d, q, r, s)
                    sb, sz = conditional(bb, phases), conditional(zz, phases)
                    self.assert_close(np.trace(sb), 1)
                    self.assert_close(np.trace(sz), 1)
                    per_setting_purity.append(purity(sb))
                    per_setting_info.append(verify.von_neumann(sb) - verify.von_neumann(sz))
                # Number-diagonal input makes different Fourier outcomes
                # related by number-phase rotations on B and Z.
                self.assert_close(per_setting_purity, per_setting_purity[0])
                self.assert_close(per_setting_info, per_setting_info[0])
                purities.append(float(np.mean(per_setting_purity)))
                infos.append(float(np.mean(per_setting_info)))
            with self.subTest(d=d, a=a, b=b):
                self.assert_close(np.mean(purities), collision_identity(bd, d, d))
                self.assertGreaterEqual(float(np.mean(infos)) + 3e-11, bound)
                selected = int(np.argmin(purities))
                self.assertLessEqual(purities[selected], collision_upper + 3e-11)
                self.assertGreaterEqual(infos[selected] + 3e-11, bound)
                self.assertGreaterEqual(max(infos) + 3e-11, bound)
                self.assertLess(float(np.dot(np.arange(d), thermal)), energy)
                if d >= 4:
                    self.assertGreater(bound, 0)


if __name__ == '__main__':
    unittest.main()
