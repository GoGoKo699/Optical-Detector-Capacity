"""Check bridge calculations and deliberately broken learning-map fixtures."""
from __future__ import annotations

import math
import unittest

import numpy as np

import check_learning as learning
import verify


def fixture() -> tuple[dict[str, str], set[str]]:
    """Small synthetic documents test the checker without claiming to be source text."""
    version = '1604.07450v5'
    texts = {path: version + '\nMILESTONES.md PRESKILL_BRIDGE.md\n' for path in learning.DOCUMENTS}
    texts['learning/README.md'] += learning.ANCHOR
    texts['learning/PRESKILL_BRIDGE.md'] += learning.ANCHOR
    chunks = [version]
    for i in range(1, 31):
        phase = 'Background/preliminaries' if i <= 14 else 'Narrative/innovation'
        dep = 'None.' if i == 1 else f'[M{i-1:02d}](#m{i-1:02d}).'
        chunks.append(f'''\n<a id="m{i:02d}"></a>
### M{i:02d} — Target {i}
**Phase:** {phase}.
**Central question:** What does this mean?
**Understanding target:** Explain this target.
**Dependencies:** {dep}
**Story role:** Connect the argument.
**Conceptual connection:** Join the objects.
**Sources:** Preskill; [science](../science/model.md).
''')
    texts['learning/MILESTONES.md'] = '\n'.join(chunks)
    return texts, set(texts) | {'science/model.md'}


class StructureChecks(unittest.TestCase):
    def test_valid_fixture(self):
        texts, paths = fixture()
        result = learning.validate_documents(texts, paths)
        self.assertEqual(result['milestones'], 30)
        self.assertEqual(result['dependency_edges'], 29)

    def assert_rejected(self, transform):
        texts, paths = fixture()
        transform(texts, paths)
        with self.assertRaises(ValueError):
            learning.validate_documents(texts, paths)

    def test_missing_or_duplicate_milestone(self):
        for replacement in ('### X30 —', '### M29 —'):
            with self.subTest(replacement=replacement):
                self.assert_rejected(lambda t, p: t.update({
                    'learning/MILESTONES.md': t['learning/MILESTONES.md'].replace('### M30 —', replacement)}))

    def test_future_dependency(self):
        self.assert_rejected(lambda t, p: t.update({
            'learning/MILESTONES.md': t['learning/MILESTONES.md'].replace('**Dependencies:** None.', '**Dependencies:** [M30](#m30).', 1)}))

    def test_wrong_phase(self):
        self.assert_rejected(lambda t, p: t.update({
            'learning/MILESTONES.md': t['learning/MILESTONES.md'].replace('**Phase:** Background/preliminaries.', '**Phase:** Narrative/innovation.', 1)}))

    def test_missing_field(self):
        self.assert_rejected(lambda t, p: t.update({
            'learning/MILESTONES.md': t['learning/MILESTONES.md'].replace('**Understanding target:** Explain this target.', '', 1)}))

    def test_broken_local_target(self):
        self.assert_rejected(lambda t, p: p.remove('science/model.md'))

    def test_broken_anchor(self):
        self.assert_rejected(lambda t, p: t.update({
            'learning/MILESTONES.md': t['learning/MILESTONES.md'].replace('](#m01)', '](#missing)', 1)}))

    def test_unpinned_source(self):
        self.assert_rejected(lambda t, p: t.update({
            'learning/README.md': t['learning/README.md'].replace(learning.ANCHOR, 'https://arxiv.org/abs/1604.07450')}))

    def test_unclosed_math_and_personal_record(self):
        for extra in ('\n```math\nx=1', '\nanswer_history'):
            with self.subTest(extra=extra):
                self.assert_rejected(lambda t, p: t.update({
                    'learning/PRESKILL_BRIDGE.md': t['learning/PRESKILL_BRIDGE.md'] + extra}))


class BridgeCalculations(unittest.TestCase):
    def test_complete_counting_example(self):
        bk, zk, residual = verify.counts(np.array([.5, .5]), .5, .25)
        np.testing.assert_allclose(bk.sum(axis=0), [.875, .125], atol=1e-14)
        np.testing.assert_allclose(bk[:, 0] / .875, [5/7, 2/7], atol=1e-14)
        np.testing.assert_allclose(zk[:, 0] / .875, [6/7, 1/7], atol=1e-14)
        info = verify.entropy(bk.ravel()) - verify.entropy(zk.ravel())
        expression = (7/8) * (verify.entropy([2/7, 5/7])-verify.entropy([1/7, 6/7]))
        self.assertAlmostEqual(info, expression, places=14)
        self.assertAlmostEqual(info, .23751681623626578, places=14)
        self.assertAlmostEqual(residual, .75, places=14)

    def test_coherent_readout_is_not_forgetting_counts(self):
        a, c = .5, .5
        a0 = np.diag([1., math.sqrt(a)])
        a1 = np.array([[0., math.sqrt(c)], [0., 0.]])
        ap, am = (a0+a1)/math.sqrt(2), (a0-a1)/math.sqrt(2)
        np.testing.assert_allclose(ap.T@ap+am.T@am, np.eye(2), atol=1e-14)
        rho = np.diag([0., 1.])
        coarse = a0@rho@a0.T+a1@rho@a1.T
        phase_branch = ap@rho@ap.T
        self.assertAlmostEqual(coarse[0,1], 0.)
        self.assertAlmostEqual(phase_branch[0,1], .25)
        np.testing.assert_allclose(phase_branch+am@rho@am.T, coarse, atol=1e-14)

    def test_thermal_entropy_purity_and_truncation(self):
        for x in (.1, 1., 5.):
            with self.subTest(mean=x):
                r=x/(1+x)
                m=1000
                n=np.arange(m+1)
                p=(1-r)*r**n
                self.assertLess(1-float(p.sum()), 1e-13)
                self.assertAlmostEqual(float(np.dot(n,p)), x, places=12)
                self.assertAlmostEqual(verify.entropy(p), verify.g(x), places=12)
                self.assertAlmostEqual(float(p@p), 1/(1+2*x), places=12)
                m=7
                n=np.arange(m+1)
                p=(1-r)*r**n
                normalized=p/p.sum()
                omitted=r**(m+1)
                exact_mean=x-(m+1)*omitted/(1-omitted)
                self.assertAlmostEqual(float(n@normalized),exact_mean,places=12)
                self.assertLess(exact_mean,x)

    def test_rare_pulse_mean_not_second_moment(self):
        for m in (2,40,400,40000):
            self.assertAlmostEqual((2/m)*m,2.)
            self.assertAlmostEqual((2/m)*m*m,2*m)


if __name__ == '__main__':
    unittest.main()
