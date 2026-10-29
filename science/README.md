# Scientific account

[Home](../README.md) · [Model](model.md) · [Sources](../references/RELATED_WORK.md)

A detector does two things: it produces a classical record and chooses which coherences survive in the signal. Counting the collected photons provides useful loss information, but irreversibly distinguishes photon-number alternatives. A coherent POVM can erase that distinction before producing its record.

The argument has four parts. [The operational reduction](capacity_reduction.md) includes arbitrary endpoint codes, establishes the inherited collective benchmark, and reduces the counting problem to an optimization over input photon-number distributions. [The counting analysis](counting_bounds.md) combines an energy-only residual-variance estimate with a loss-dependent thinning bound and a matching thermal-input construction. [The coherent construction](coherent_measurements.md) derives a purity identity, reproduces it with an established quadratic-phase design, and selects one Fourier measurement with linearly many coded outcomes. [The uniform laws](uniform_laws.md) put these bounds together and certify a finite-energy separation. The [two-photon bridge](qubit_optical_bridge.md) separately locates a finite-cutoff failure of the vacuum/one-photon counting optimum. The [resource account](detector_resources.md) gives an explicit cutoff, matches the leading helper-record cost, and bounds the effect of finite control error.

## Dependencies

The [model](model.md) owns all resources and the meanings of $`Q_{\rm cnt},Q_1,Q_{\rm coll}`$.

| Conclusion | Required ingredients |
|---|---|
| Collective benchmark | Joint output degradation, a direct arbitrary-encoder converse, thermal relative-entropy contraction, inherited assistance and energy-constrained coding |
| Exact counting variational formula | Degradability of the flagged channel, phase averaging, energy-constrained coding |
| Counting energy upper bound | Multinomial residual second moment and the integer entropy/variance bound |
| Counting loss upper bound | Thinning mutual-information identity, row-sum entropy gain, binomial collision estimate |
| Counting lower bound | Conditional negative-binomial law, its collision integral, geometric logarithmic-moment bound |
| Individual-mode lower bound | Finite POVM completeness, exact phase-averaged purity, entropy ordering, charged signal-energy cutoff |
| Constant gap and uniform exponents | The preceding finite inequalities and elementary bounds on thermal entropy |
| Linear reference stock for communication | Conditional shifted-sine entropy, actual complementary output, receiver entropy concavity, and finite-cutoff coding |
| Local-reference fluctuation ceiling | Refinement by each local conserved number, logical-reference entropy, multinomial residual variance, and mean-energy averaging |
| Mean reference-energy profile | The same conserved-number refinement, first absolute residual moment, conditional dither/Laplace entropy bound, and the direct sine construction |

Primary coding and assistance theorems retain their [attribution](../references/RELATED_WORK.md). Finite matrix calculations do not prove channel coding. The construction's finite support is used for achievability only; the converse never restricts competing inputs to that support.

The resource extensions also give the classical-record tradeoff to a uniform
additive constant. The [finite reference](finite_reference.md) applies an
established conserving gate construction and energy theorem to the prescribed
Fourier detector, and keeps that gate-level result distinct from the capacity
optimization over all possible measurements.

The [direct apparatus argument](direct_reference.md) pays discarded-reference
entropy directly and uses a reference of linear mean energy at fixed rate gap.
The [local-reference converse](reference_width_bounds.md) applies to arbitrary
codes and coherent inputs under the stated per-mode conservation contract. It
matches the required support-width order in the energy-driven regime. The
[mean-stock converse](reference_mean_bounds.md) separately uses a first absolute
moment, including infinite-variance references, and matches the linear initial
mean-energy order. Together the upper bound and direct construction give the
complete mean-stock capacity profile to an additive constant in that regime.
