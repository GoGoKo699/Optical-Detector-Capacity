# Optical Detector Capacity

**Can reading lost light one mode at a time recover the leading quantum communication rate?** Yes, but photon counting and coherent measurements have different limits.

A vacuum optical splitter sends a fraction $`a`$ of the signal to the receiver, a fraction $`b`$ to an inaccessible output, and $`c=1-a-b`$ to a helper. The helper measures its output and sends only a classical record to the receiver. The signal budget is $`E`$ mean photons per original mode. Both detector classes permit arbitrary sender and receiver block codes.

For fixed $`0<a<1`$, increasing energy and approaching complete collection give, uniformly with $`L=\min\{E,1/b\}`$ and $`1/0=\infty`$,

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

The [structured detector construction](science/coherent_measurements.md) retains this rate guarantee using one preselected quadratic phase followed by a finite Fock-space Fourier measurement. At cutoff dimension $`d\ge2`$, fewer than $`2d`$ outcomes have nonzero probability on the coded support. The [qubit-to-optical bridge](science/qubit_optical_bridge.md) also shows that a three-outcome detector already beats optimized counting when inputs are restricted to at most two photons.

The [resource account](science/detector_resources.md) makes the cutoff and accuracy quantitative. At fixed additive tolerance, $`O(L+1)`$ cutoff levels and $`\log_2L+O(1)`$ helper record bits per mode suffice; recovering the full leading rate requires that same leading record cost. It also bounds rate loss from detector error and accounts for the specified Fourier stage's change in mean photon number.

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
| Why does counting have the half-logarithmic law? | [Counting bounds and construction](science/counting_bounds.md) |
| How can one collected mode retain the full leading rate? | [Finite coherent POVM](science/coherent_measurements.md) |
| Where does the qubit counting optimum first fail? | [Two-photon separation](science/qubit_optical_bridge.md) |
| What cutoff, record length, and control accuracy suffice? | [Detector resources](science/detector_resources.md) |
| What is uniform as energy and inaccessible loss vary? | [Uniform laws](science/uniform_laws.md) |
| What changes physically, and what remains outside the result? | [Interpretation](science/interpretation.md) |
| Which ingredients and comparisons are inherited? | [Related work](references/RELATED_WORK.md) |
| How are the finite calculations reproduced? | [Verification](verification/README.md) |

The collective optical capacity is inherited from the [partial-monitoring analysis](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/tree/447726d37438de67b4ef2e1a9406d2c44d6a394f). The detector-class comparison, its uniform counting converse, and the constant-gap single-mode construction are the subject here.

## Learn the project

The single educational anchor is **John Preskill, *Quantum Shannon Theory*, Chapter 10, arXiv:1604.07450v5** (updated June 2025; posted 8 July 2025). The [learning entrance](learning/README.md) gives a focused route rather than a whole-chapter assignment.

The [30-milestone map](learning/MILESTONES.md) connects **14 background/preliminaries milestones** to **16 narrative/innovation milestones**. It progresses from optical states and entropy to the complete detector-capacity comparison. Every milestone has an understanding target, earlier dependencies, a conceptual connection, and source pointers.

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

The base model assumes vacuum ancillary inputs, memoryless splitting, unlimited reliable helper-to-receiver classical communication, and unrestricted endpoint quantum coding. The resource corollary separately prices the transmitted classical record and bounds sufficient control accuracy. The coherent detector may use a phase reference and general non-Gaussian control; physical synthesis, reference preparation, and reset costs remain open. The energy budget prices the signal, not the measurement apparatus. No feedback to the sender or postselection is supplied.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
