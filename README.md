# Optical Detector Capacity

**Can reading lost light one mode at a time recover the leading quantum communication rate?** Yes, but photon counting and coherent measurements have different limits.

A vacuum optical splitter sends a fraction $`a`$ of the signal to the receiver, a fraction $`b`$ to an inaccessible output, and $`c=1-a-b`$ to a helper. The helper measures its output and sends only a classical record to the receiver. The signal budget is $`E`$ mean photons per original mode. Both detector classes permit arbitrary sender and receiver block codes.

For fixed $`0\lt a\lt 1`$, increasing energy and approaching complete collection give, uniformly with $`L=\min\{E,1/b\}`$ and $`1/0=\infty`$,

```math
Q_{\rm cnt}(E)=\frac12\log_2 L+O_a(1),
\qquad
Q_1(E)=Q_{\rm coll}(E)+O(1)=\log_2 L+O_a(1).
```

Here $`Q_{\rm cnt}`$ allows exact photon counting and arbitrary processing of the entire count record. $`Q_1`$ permits predetermined individual-mode POVMs, including coherent superpositions of different photon numbers. $`Q_{\rm coll}`$ permits joint measurements of all collected modes. The [uniform domain](science/uniform_laws.md) keeps $`a`$ fixed and includes $`b=0`$.

At every finite energy, not just in this limit,

```math
0\le Q_{\rm coll}(E)-Q_1(E)\le\log_2 e.
```

Thus joint processing across collected modes improves on the best individual-mode detector by at most about $`1.443`$ qubits per mode. Counting instead loses an unbounded amount as $`L`$ grows. The distinction is between coherence across photon numbers **within a mode** and processing **across modes**. Counting itself is non-Gaussian; this is not a general Gaussian-versus-non-Gaussian comparison.

The [coherent detector](science/coherent_measurements.md) can use one preselected quadratic phase followed by a finite Fock-space Fourier measurement, with fewer than $`2d`$ occupied outcomes at cutoff dimension $`d`$. A [three-outcome example](science/qubit_optical_bridge.md) already separates coherent detection from optimized counting under a two-photon input cutoff. The full leading-rate theorem concerns the larger, mean-energy-only input class.

## How much phase reference is needed?

The [reference-energy extension](science/reference_mean_bounds.md) charges the apparatus that enables coherent detection. Let $`M`$ be its average **initial mean photon number per channel use**. The initial apparatus is independent of the encoded signal, and each effective helper measurement preserves every local total $`N_{D_i}+N_{W_i}`$. Classical records remain unrestricted. Under this separate-local-invariance contract,

```math
Q_{\rm loc}^{\rm mean}(E,M)
=\min\!\left\{\log_2E,
\max\!\left\{\tfrac12\log_2E,\log_2(M+1)\right\}\right\}+O_a(1).
```

The formula holds uniformly for fixed $`0\lt a\lt 1`$, $`E\ge1`$, $`M\ge0`$, $`0\le b\le\frac12\min\{a,1-a\}`$, and $`bE\le1`$. It characterizes capacity to an additive constant depending only on $`a`$.

Counting supplies the half-logarithmic rate without a coherent reference. A bounded additive gap to the full logarithm is attainable with $`M=O(E)`$ and requires $`M=\Omega(E)`$. The [construction](science/direct_reference.md) uses fresh finite sine references; the converse includes arbitrary endpoint codes and references with infinite variance. Merely preserving the sum of all modes' photon numbers is a broader operation class, outside this profile.

The [resource account](science/detector_resources.md) separately quantifies the required classical record, cutoff, and control accuracy. The [support-width bound](science/reference_width_bounds.md) distinguishes reference spread from mean stock, and the [conserving realization](science/finite_reference.md) makes the detector's photon exchange explicit. These results price prepared photons and transmitted records; they do not determine preparation work, reset cost, or sustained coherent reuse.

## Finite-energy separation

At $`a=1/4`$, $`b=1/10000`$, and $`E=10^6`$:

| Quantity | Rigorous comparison, qubits per mode |
|---|---:|
| Counting capacity, optimized over all allowed inputs and codes | Less than 7.90 |
| Achievable capacity with coherent individual-mode measurements | Greater than 10.51 |
| Collective helper capacity | Between 11.28 and 11.29 |

The [certificate](verification/README.md) uses rational logarithm enclosures. These are capacity bounds, not an implemented code or a laboratory operating point. The counting upper bound includes rare, arbitrarily large photon numbers under the mean budget.

## Read the science

Start with the [physical model and claims](science/model.md), then follow the [connected proof route](science/README.md).

| Question | Authoritative account |
|---|---|
| What information, controls, and energy are supplied? | [Model](science/model.md) |
| Why do arbitrary codes obey the entropy bounds? | [Operational reduction](science/capacity_reduction.md) |
| Why do the two detector classes have different leading rates? | [Counting bounds](science/counting_bounds.md) and [coherent construction](science/coherent_measurements.md) |
| Where does the qubit counting optimum first fail? | [Two-photon separation](science/qubit_optical_bridge.md) |
| What is uniform as energy and inaccessible loss vary? | [Uniform laws](science/uniform_laws.md) |
| What does a finite apparatus budget buy? | [Mean-reference capacity profile](science/reference_mean_bounds.md) and [connected resource proofs](science/README.md) |
| What remains outside the comparison, and which results are inherited? | [Interpretation](science/interpretation.md) and [related work](references/RELATED_WORK.md) |
| How are the finite calculations reproduced? | [Verification](verification/README.md) |

The collective optical capacity is inherited from the [partial-monitoring analysis](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/tree/447726d37438de67b4ef2e1a9406d2c44d6a394f). The detector-class comparison, its uniform counting converse, and the constant-gap single-mode construction are the subject here.

## Learn the project

The single educational anchor is **John Preskill, *Quantum Shannon Theory*, Chapter 10, arXiv:1604.07450v5** (updated June 2025; posted 8 July 2025). The [learning entrance](learning/README.md) gives a focused route rather than a whole-chapter assignment.

The [30-milestone map](learning/MILESTONES.md) connects **14 background/preliminaries milestones** to **16 narrative/innovation milestones**. It progresses from optical states and entropy through the detector comparison to the finite-reference capacity profile. Every milestone has an understanding target, earlier dependencies, a conceptual connection, and source pointers.

The [Preskill bridge](learning/PRESKILL_BRIDGE.md) translates notation, works through an explicit counting channel, and explains the additional optical, finite-energy, and detector arguments. In particular, Preskill's one-use coherent-information quantity is not this project's individual-mode helper capacity. The science pages remain the authoritative proofs; the learning route does not replace their assumptions or primary-source attribution.

## Reproduce

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
python verification/check_learning.py
python -m unittest discover -s verification -p "test_*.py" -v
python verification/qutrit_certificate.py
```

The runner checks finite channel identities, complete finite POVMs, entropy inequalities, and the rational rate certificate. The [learning checks](learning/README.md#reproduce-the-learning-checks) validate the milestone structure, links, and worked examples. Written proofs establish the arbitrary-input and asymptotic statements. [Verification scope](verification/README.md) distinguishes these roles. The [review record](verification/FURNISHING_CHECK.md) states performed checks and remaining display-verification limits.

## Scope

The base model assumes vacuum ancillary inputs, memoryless splitting, unlimited reliable helper-to-receiver classical communication, and unrestricted endpoint quantum coding. Its energy budget $`E`$ prices the signal. The resource extensions separately charge reference mean photons or the transmitted record under their stated contracts. General coherent control remains allowed; physical synthesis, preparation work, and reset costs are not optimized. No sender feedback or outcome postselection is supplied.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
