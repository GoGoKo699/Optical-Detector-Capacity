# Scientific account

[Home](../README.md) · [Model](model.md) · [Sources](../references/RELATED_WORK.md)

A detector produces a classical record and determines which photon-number
coherences survive. The first question is how that choice changes communication
capacity. The second is how much prepared phase reference is needed to obtain
the coherent detector's advantage. The [model](model.md) defines the base
comparison; each resource extension states its additional operation and budget
constraints.

## From the optical channel to the detector comparison

Read the following pages in order. The counting and coherent branches meet at
the same inherited collective benchmark and the same mean signal budget.

| Page | Role in the argument |
|---|---|
| [Operational reduction](capacity_reduction.md) | Joint output degradation, arbitrary-encoder converse, inherited collective capacity, and exact counting reduction |
| [Counting bounds](counting_bounds.md) | Energy-only residual estimate and loss-dependent thinning converse, matched by a thermal-input construction |
| [Coherent measurements](coherent_measurements.md) | Complete finite phase POVM, purity identity, inherited quadratic design, and selection of one Fourier setting |
| [Uniform laws](uniform_laws.md) | Counting's half logarithm, the coherent full logarithm, the constant collective gap, and the certified finite comparison |
| [Qubit-to-optical bridge](qubit_optical_bridge.md) | A separate two-photon-cutoff example locating the first failure of the vacuum/one-photon counting optimum |

The cutoff in an achievable construction is not imposed on competing codes.
The two-photon example explicitly adds its own per-mode cutoff; it is not a
counting upper bound under the unrestricted mean-energy-only model.

## From a coherent detector to a charged reference budget

The finite apparatus and its discarded systems belong to the channel. Keeping
them explicit connects a constructive detector to a capacity bound on every
allowed protocol.

| Page | Resource and proof mechanism |
|---|---|
| [Detector resources](detector_resources.md) | Explicit cutoff and accuracy bounds, complete classical-record accounting, and the record-capacity tradeoff |
| [Finite reference](finite_reference.md) | Established sine-reference and number-conserving lift for the prescribed Fourier gate; uniform gate error and photon exchange |
| [Direct reference bound](direct_reference.md) | Conditional shifted-sine entropy bounds the actual discarded reference; a linear initial mean stock suffices for communication |
| [Reference-width bounds](reference_width_bounds.md) | Separate local invariance permits conserved-number refinement; a residual variance estimate gives all-code spread and width bounds |
| [Reference-mean bounds](reference_mean_bounds.md) | A first absolute residual moment, conditional dither/Laplace entropy, and the direct construction give the complete mean-budget profile |

The last two converses require each effective helper effect to commute with
every local total $`N_{D_i}+N_{W_i}`$. They permit arbitrary endpoint codes and
initial references independent of the signal. Global-total-only invariance is
a broader class. The mean-budget proof covers infinite reference variance;
variance alone would not establish that mean-energy conclusion.

The mean and width profiles use the energy-driven domain $`E\ge1`$,
$`bE\le1`$, and $`0\le b\le\frac12\min\{a,1-a\}`$ at fixed $`a`$.
The record tradeoff is a separate optimization. Combining the individual
profiles does not establish a joint record-and-reference frontier.

## Attribution and verification

The collective optical capacity comes from Partial Monitoring. Assistance,
coding, phase designs, and the conserving reference construction retain their
[primary-source attribution](../references/RELATED_WORK.md). The
[interpretation](interpretation.md) explains the physical scope and remaining
implementation questions.

The [verification account](../verification/README.md) maps finite calculations
to the written proofs. Rational certificates evaluate particular inequalities;
matrix tests check channel identities and complete complementary outputs.
The universal and asymptotic claims rely on the written arguments and the
cited coding theorems.
