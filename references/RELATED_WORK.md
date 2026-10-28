# Related work and attribution

[Home](../README.md) · [Scientific route](../science/README.md) · [Bibliography](references.bib)

The contribution is the optimized **detector-class comparison** for the vacuum splitter: an input-uniform counting converse, a matching half-logarithmic construction, and a finite single-mode coherent measurement within a constant of the collective capacity. Environmental assistance, flagged-channel coding, random-phase ensembles, Gaussian entropy formulas, and the qualitative benefit of non-Gaussian measurements are established ingredients.

## The closest internal antecedent

The [Partial-Monitoring-Capacity scientific account](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/447726d37438de67b4ef2e1a9406d2c44d6a394f/research/THEOREM.md), at revision `447726d37438de67b4ef2e1a9406d2c44d6a394f`, supplies the collective optical capacity, the helper-preserving degradation identity, and the thermal-reference argument. Its [proof dependencies](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/447726d37438de67b4ef2e1a9406d2c44d6a394f/research/PROOF_DEPENDENCIES.md) and [coarse-record converse](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/447726d37438de67b4ef2e1a9406d2c44d6a394f/research/CLAIM_ASSESSMENT_2026-10-07.md) retain arbitrary encoders and inaccessible outputs. Those results are inherited here, not counted as a second contribution.

Its [product-measurement theorem](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/447726d37438de67b4ef2e1a9406d2c44d6a394f/research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) concerns a **qubit** excitation splitter. It optimizes over all predetermined single-use helper POVMs and proves counting optimality there; it explicitly does not extend that conclusion to optical modes. The present all-input optical counting bounds and coherent-detector construction resolve a different behavior in the unbounded Fock space. Their rate separation is not an application of the qubit optimum.

Two other nearby projects have different operational tasks. [Bosonic-Phase-Memory](https://github.com/GoGoKo699/Bosonic-Phase-Memory) optimizes one-use logical storage under unobserved phase noise, without a helper output. [Atomtronic-Isolation-Quantum-Limits](https://github.com/GoGoKo699/Atomtronic-Isolation-Quantum-Limits) studies active Gaussian scattering and a two-way entanglement/key boundary. Neither provides the passive receiver-only counting-versus-coherent rate comparison.

## Assistance and coding ingredients

### Smolin, Verstraete, and Winter (2005)

[Entanglement of assistance and multipartite state distillation](https://arxiv.org/abs/quant-ph/0505038), Physical Review A **72**, 052317. Theorem 1 supplies the regularized minimum-entropy assistance result; Theorem 8 turns a fixed environmental measurement into a flagged channel and applies ordinary quantum coding. The paper also uses coherent superpositions and random coding. These methods and receiver-only assistance are inherited. Here a single collected mode is measured, inaccessible loss remains in the coherent information, and the construction is compared with the **optimized** number detector rather than a chosen input example. The inspected primary PDF was arXiv v1, Theorems 1 and 8 and the associated construction.

### Wilde and Qi (2018)

[Energy-constrained private and quantum capacities of quantum channels](https://arxiv.org/abs/1609.01997v2), IEEE Transactions on Information Theory **64**, 7802–7827. Theorem 2 supplies energy-constrained coherent-information achievability; Theorem 3 identifies the single-letter capacity of a degradable channel under the Gibbs-observable and finite-output-entropy conditions. The counting channel satisfies those conditions. Finite-support coherent detectors satisfy them on their coded input spaces. The thermal-reference method in Section X is also inherited. The primary v2 statements, hypotheses, and relevant proof passages were inspected. They do not perform the present optimization over detector classes.

### Winter (2016)

[Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints](https://arxiv.org/abs/1507.07775v6), Communications in Mathematical Physics **347**, 291–313. Lemma 2 supplies continuity of conditional entropy with dependence on the finite reference dimension, not the conditioning-system dimension. It justifies the finite-record limit and the transmission converse. Thermal-tail convergence in the constructive argument is additionally derived from entropy-of-mixture bounds. The primary v6 lemma and proof were inspected.

## Closest optical measurement comparisons

### Fiurášek and Mišta (2007)

[Gaussian localizable entanglement](https://arxiv.org/abs/0706.2799v1), Physical Review A **75**, 060302(R). The paper optimizes Gaussian localization in specified state families and demonstrates an improvement using photon counting. Its final example, including Eq. (15), prepares Fock states by measuring a squeezed-state partner and splits them on a balanced beam splitter, producing binomial Schmidt entropies. Thus counting-induced entanglement and binomial-entropy behavior are prior art. That example does not optimize a quantum transmission channel over all mean-energy-constrained inputs, nor prove a uniform converse with inaccessible residual loss. The primary four-page text, including that example, was inspected.

### Lami, Takagi, and Adesso (2020)

[Assisted concentration of Gaussian resources](https://arxiv.org/abs/1905.02173v2), Physical Review A **101**, 052305. Theorem 11 and Section VI compare Gaussian and general assistance for specified states when the helper holds a purification. For equal-temperature product thermal states, they give a high-energy constant gap between the Gaussian and unrestricted assisted entanglement values. Section VI also credits photon-counting advantages from earlier localization work. This is a substantive precedent for quantitative assistance comparisons, not the present counting-versus-coherent channel theorem: the resource restriction, source state, inaccessible subsystem, and optimized objective differ. The primary v2 theorem and Section VI were inspected; their qualitative message is not claimed as new here.

### Input-environment preparation is a different resource

Wang and Jiang, [Passive environment-assisted quantum communication with GKP states](https://arxiv.org/abs/2401.16781v2), Physical Review X **15**, 021003 (2025), improve transmission by preparing the *incoming* environment. Voss, Li, Wang, and Jiang, [Passive Environment-Assisted Quantum Communication](https://arxiv.org/abs/2602.21549v2) (2026), further study non-Gaussian ancilla inputs. Their primary abstracts identify this different access model. Here every unused input is vacuum and the helper only measures collected *outgoing* light. These sources were screened for their operational setup, not audited in full, and are not imported proof ingredients.

## What remains after attribution

The mathematical additions are the residual-variance and thinning converses uniform over all finite-mean photon distributions; their match by a negative-binomial counting construction; the finite fourth-root-phase POVM and its one-mode purity bound; and the resulting uniform energy/loss crossover and finite-energy capacity separation. The elementary entropy inequalities are derived locally as tools, without a separate priority claim for those inequalities. The collective capacity itself and general assistance methodology are credited above.

The principal consequence distinguishes coherence *within* one collected mode from coherent processing *across* many modes. It does not assert that Gaussian detectors are optimal, that every non-Gaussian detector helps, or that the exhibited finite POVM has an efficient implementation.

## Coverage of the comparison

The comparison was checked on **28 October 2026**. It follows the assistance, energy-constrained coding, Gaussian localization, and optical environment-access lines above, together with the named internal antecedents. Searches included bosonic environmental monitoring, photon-counting quantum capacity, and single-mode assistance. No inspected source supplied the same all-input detector-class law under the stated access and energy contract. This is a bounded comparison, not an exhaustive priority certificate. PDF text was available for the principal comparisons; attempted PDF screenshots failed in this environment, so no visual inspection of their figures is claimed. Unavailable figures were not used to establish a theorem comparison.
