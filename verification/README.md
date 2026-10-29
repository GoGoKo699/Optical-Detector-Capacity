# Reproduce the finite checks

[Home](../README.md) · [Scientific dependencies](../science/README.md)

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
python -m unittest discover -s verification -p 'test_*.py' -v
python verification/qutrit_certificate.py
```

The reference environment is Python **3.13.5** and NumPy **2.3.5**. The suite is deterministic and has no network or input-data dependency. It compares its computed record with the committed [expected.json](expected.json); a missing or changed reference is an error. Checks use explicit exceptions, not Python assertions that disappear in optimized mode. Paths resolve relative to the script, so it also runs from another working directory.

To retain a separate output, use a new path:

```bash
python verification/verify.py --output /path/to/new-result.json
```

The runner refuses to overwrite the expected record or an existing output. Do not refresh the reference merely to make a failing calculation pass.

## Claim-to-check map

| Component | Finite check | What establishes the general claim |
|---|---|---|
| Counting reduction and energy converse | 20 multinomial inputs checking entropy/thinning identities and residual second moments; a separate rare-pulse thinning test | [Arbitrary-code reduction](../science/capacity_reduction.md) and [counting proof](../science/counting_bounds.md) |
| Binomial entropy envelope | 90 parameter cases, including deterministic and strongly skewed laws | Collision-integral and integer-variance proofs |
| Coherent detector | All 64 or 256 fourth-root outcomes in three finite cases; POVM completeness, joint degradation, normalization, and exact mean-purity identity | [Finite-POVM proof and cutoff limit](../science/coherent_measurements.md) |
| Structured detector | Exact modular fourth-moment pairing for dimensions 2 through 12; invalid-modulus counterexamples; Fourier effects, mixed-state purity, and five optical fixed-setting cases | [Quadratic design and selected-setting proof](../science/coherent_measurements.md#quadratic-phases-reproduce-the-same-moments) |
| Two-photon comparison | Rational logarithm and square-root enclosures for a coherent rate and a global concavity-tangent counting upper bound; independent full-isometry branch reconstruction and optimized-Python certificate execution | [Finite-cutoff channel reduction and certificate](../science/qubit_optical_bridge.md) |
| Detector resources | Finite-cutoff purity/tail bounds, full-reference noisy instruments, mixed encoders and message entropy, and Fourier excitation change | [Cutoff, accuracy, and record proofs](../science/detector_resources.md) |
| Record tradeoff | Actual cutoff channels and selected settings under feasible alphabet budgets; scalar cases with nonvacuous additive bounds | [Uniform additive tradeoff](../science/detector_resources.md#the-finite-record-tradeoff-to-an-additive-constant) |
| Finite reference | Conserving sector unitary, both ladder boundaries, sine moments, Choi/phase-mixture identity, entangled-input errors, and actual optical reference state | [Reference construction and inherited gate-energy bound](../science/finite_reference.md) |
| Direct reference rate | Dirichlet spectra and gaps, arbitrary translated-sine mixtures, requested entropy penalties, and actual optical channels with discarded references | [Communication-specific entropy proof](../science/direct_reference.md) |
| Reference fluctuations | Coherent signal inputs, mixed reference states, invariant detector refinements, exact estimator MSE, and logical-reference entropy bounds | [All-code local conservation bound](../science/reference_width_bounds.md) |
| Mean reference stock | Actual coherent-input invariant channels, conditional dither entropy, sparse reference tails, unequal-use budgets, and feasible sine-reference sizes | [First-moment converse and matched mean profile](../science/reference_mean_bounds.md) |
| Counting construction | 20 negative-binomial cases; probability and collision tail bounds | Negative-binomial integral bound and geometric lower-tail argument |
| Scalar bounds | 175 parameter cases comparing lower bounds with the inherited collective value and constant-gap inequality | [Uniform theorem](../science/uniform_laws.md), not extrapolation from the grid |
| Finite-energy separation | Exact rational interval certificate, independent of floating-point comparison | Analytical bounds plus the certified logarithms |

The matrix cases test finite input cutoffs, not a transmitted quantum code or a laboratory detector. Floating-point identities use the stated tolerances in the script. The grid does not establish optimality over all inputs, large-energy asymptotics, or an implementation complexity bound.

## Rational finite-energy certificate

At receiver fraction $`1/4`$, inaccessible fraction $`1/10000`$, and mean signal occupation $`10^6`$, the script proves

```math
Q_{\rm cnt}<7.90,

Q_1>10.51,

11.28<Q_{\rm coll}<11.29.
```

Every logarithm in this certificate is enclosed using rational range reduction and 48 terms of

```math
\ln x=2\sum_{j=0}^{47}\frac{z^{2j+1}}{2j+1}+R,
\qquad z=\frac{x-1}{x+1},
\qquad |R|\le\frac{2|z|^{97}}{97(1-z^2)}.
```

Range reduction gives $`1\le x\le2`$ and $`|z|\le1/3`$. The code uses $`\pi<22/7`$ in the upper bound and $`\log_2e=1/\ln2`$. The comparisons with the decimal thresholds are comparisons of integers and fractions. Displayed decimal endpoints are summaries, not floating-point premises. The implied capacity separation exceeds **2.61 qubits per original mode**.

The logarithm intervals certify these finite bound evaluations; they are not a formal certificate of the infinite-dimensional channel theorem. The analytic account carries that responsibility. No experimental validation or independent external proof review is asserted.
