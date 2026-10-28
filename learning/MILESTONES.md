# Thirty-milestone understanding map

[Home](../README.md) · [Learning entrance](README.md) · [Preskill bridge](PRESKILL_BRIDGE.md) · [Scientific route](../science/README.md)

The map has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. The background joins optical carriers, classical records, entropy, and coding into one resource model. The narrative then develops the counting and coherent-detector arguments separately before joining them into the uniform comparison. The allocation follows that scientific structure, not a particular reader's preparation.

Every dependency points to an earlier milestone. The targets cover the connected argument, not every technical lemma. Preskill section references use **arXiv:1604.07450v5**, updated June 2025 and posted 8 July 2025. The [source map](PRESKILL_BRIDGE.md#sources) distinguishes chapter foundations from optical and research arguments supplied locally.

## Background and preliminaries — M01–M14

<a id="m01"></a>
### M01 — Optical modes and number states

**Phase:** Background/preliminaries.

**Central question:** What does one use of the optical channel contain?

**Understanding target:** Identify a single oscillator mode, its number basis, and the distinction between one mode and a qubit truncation.

**Dependencies:** None.

**Story role:** Start from the physical carrier before introducing a communication protocol.

**Conceptual connection:** A mode has unbounded photon-number support even though one channel use is counted once.

**Sources:** Preskill §§10.2; [project bridge](PRESKILL_BRIDGE.md#optics); [scientific account](../science/model.md).

<a id="m02"></a>
### M02 — States and the mean photon budget

**Phase:** Background/preliminaries.

**Central question:** What does the energy allowance constrain?

**Understanding target:** Compute mean occupation from a density operator and distinguish a mean constraint from a peak, variance, or detector-energy limit.

**Dependencies:** [M01](#m01).

**Story role:** Attach the charged resource to the carrier.

**Conceptual connection:** Rare high-number pulses can obey the same mean constraint as low-number mixtures.

**Sources:** Preskill §§10.2.5; [project bridge](PRESKILL_BRIDGE.md#optics); [scientific account](../science/model.md).

<a id="m03"></a>
### M03 — The vacuum splitter

**Phase:** Background/preliminaries.

**Central question:** How does one input produce three correlated outputs?

**Understanding target:** Track the received, inaccessible, and collected fractions; derive the multinomial probabilities for a number-state input.

**Dependencies:** [M01](#m01), [M02](#m02).

**Story role:** Turn the carrier into the concrete physical channel.

**Conceptual connection:** Photon-number probabilities come from an isometry that also preserves coherence between input alternatives.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#optics); [scientific account](../science/model.md).

<a id="m04"></a>
### M04 — A reference defines quantum transmission

**Phase:** Background/preliminaries.

**Central question:** What must survive for transmission to be quantum?

**Understanding target:** Explain preservation of entanglement with an inaccessible reference and why detecting or recreating classical labels is insufficient.

**Dependencies:** [M02](#m02), [M03](#m03).

**Story role:** Fix the operational success criterion.

**Conceptual connection:** The average coded input can be mixed even when the transmitted reference-input state is pure.

**Sources:** Preskill §§10.7.1–10.7.2; [project bridge](PRESKILL_BRIDGE.md#notation); [scientific account](../science/model.md).

<a id="m05"></a>
### M05 — POVMs and conditional states

**Phase:** Background/preliminaries.

**Central question:** How does the helper measurement change the receiver state?

**Understanding target:** Distinguish a POVM effect, its outcome probability, and the normalized conditional output; include every outcome.

**Dependencies:** [M03](#m03), [M04](#m04).

**Story role:** Introduce the operation that separates the detector classes.

**Conceptual connection:** Coherently combining number alternatives before measurement is different from forgetting a classical count afterward.

**Sources:** Preskill §§10.2.2; 10.6.1; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m06"></a>
### M06 — The complete complementary output

**Phase:** Background/preliminaries.

**Central question:** Where does the measurement record go in a channel dilation?

**Understanding target:** Identify the receiver flag and its complementary copy after a rank-one measurement, and the additional unresolved system for a coarse measurement.

**Dependencies:** [M04](#m04), [M05](#m05).

**Story role:** Prevent an incomplete environmental entropy ledger.

**Conceptual connection:** The inaccessible optical mode alone is not the complement of the measured channel.

**Sources:** Preskill §§10.7.1; 10.7.3; [project bridge](PRESKILL_BRIDGE.md#flags); [scientific account](../science/capacity_reduction.md).

<a id="m07"></a>
### M07 — Classical conditional entropy

**Phase:** Background/preliminaries.

**Central question:** What uncertainty remains after the photon count is known?

**Understanding target:** Use joint, conditional, and mutual information for the count variables and distinguish a conditional average from selecting successful events.

**Dependencies:** [M03](#m03), [M05](#m05).

**Story role:** Prepare the counting channel calculation.

**Conceptual connection:** The helper count is side information at the decoder, not a free label at the encoder.

**Sources:** Preskill §§10.1.1–10.1.2; [project bridge](PRESKILL_BRIDGE.md#counting-example); [scientific account](../science/counting_bounds.md).

<a id="m08"></a>
### M08 — Quantum entropy and purity

**Phase:** Background/preliminaries.

**Central question:** Which spectral quantities control a conditional quantum state?

**Understanding target:** Relate von Neumann entropy to eigenvalues, concavity, and the lower bound by collision entropy; distinguish quantum from classical conditioning.

**Dependencies:** [M02](#m02), [M06](#m06), [M07](#m07).

**Story role:** Supply the entropy language for both detector classes.

**Conceptual connection:** A computable second moment can give an achievable-rate lower bound without diagonalizing every conditional state.

**Sources:** Preskill §§10.2.1–10.2.3; 10.9; [project bridge](PRESKILL_BRIDGE.md#thermal); [scientific account](../science/coherent_measurements.md).

<a id="m09"></a>
### M09 — Thermal states as energy references

**Phase:** Background/preliminaries.

**Central question:** Why is a thermal distribution useful even for nonthermal codes?

**Understanding target:** Derive the geometric number distribution, its entropy and purity, and its maximum-entropy role at fixed mean occupation.

**Dependencies:** [M02](#m02), [M08](#m08).

**Story role:** Connect oscillator energy to entropy bounds.

**Conceptual connection:** A thermal average input is a coding choice; a thermal reference in a converse does not restrict competing inputs.

**Sources:** Preskill §§10.2.5; [project bridge](PRESKILL_BRIDGE.md#thermal); [scientific account](../science/capacity_reduction.md).

<a id="m10"></a>
### M10 — Data processing and correlations

**Phase:** Background/preliminaries.

**Central question:** Why can local processing not improve the relevant information comparison?

**Understanding target:** Apply mutual-information and relative-entropy contraction while keeping the registers and reference states explicit.

**Dependencies:** [M06](#m06), [M07](#m07), [M08](#m08), [M09](#m09).

**Story role:** Build the inequality mechanism used in capacity converses.

**Conceptual connection:** A channel that reproduces one marginal need not preserve its joint correlations with the helper.

**Sources:** Preskill §§10.1.4; 10.2.3–10.2.4; [project bridge](PRESKILL_BRIDGE.md#degradation); [scientific account](../science/capacity_reduction.md).

<a id="m11"></a>
### M11 — Coherent information of a flagged channel

**Phase:** Background/preliminaries.

**Central question:** Which entropy difference becomes a transmission rate?

**Understanding target:** Obtain the difference of conditional receiver and complement entropies and distinguish this quantity from a detector-class capacity.

**Dependencies:** [M04](#m04), [M06](#m06), [M08](#m08), [M10](#m10).

**Story role:** Join the physical measurement and channel-coding descriptions.

**Conceptual connection:** The identical classical flag entropy cancels only when the complete complement is used.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#flags); [scientific account](../science/capacity_reduction.md).

<a id="m12"></a>
### M12 — Degradability and the zero-rate side

**Phase:** Background/preliminaries.

**Central question:** When can the environment be simulated, and what follows?

**Understanding target:** Distinguish degradation from antidegradation, explain additivity for a fixed degradable channel, and connect symmetric extensions to no cloning.

**Dependencies:** [M10](#m10), [M11](#m11).

**Story role:** Prepare the all-code counting reduction and the zero-capacity boundary.

**Conceptual connection:** An additivity proof for a fixed detector does not by itself optimize over different detectors.

**Sources:** Preskill §§10.7.3; [project bridge](PRESKILL_BRIDGE.md#degradation); [scientific account](../science/capacity_reduction.md).

<a id="m13"></a>
### M13 — Coding and limits under an energy constraint

**Phase:** Background/preliminaries.

**Central question:** How does a finite construction give an asymptotic capacity bound?

**Understanding target:** Separate code blocklength, photon cutoff, and signal energy; keep energy slack and explain why entropy convergence needs more than trace-norm convergence.

**Dependencies:** [M09](#m09), [M11](#m11), [M12](#m12).

**Story role:** Connect finite calculations to their operational use.

**Conceptual connection:** The finite cutoff belongs to an achievable construction, not to the class of competing codes in a converse.

**Sources:** Preskill §§10.7.1–10.7.2; 10.9.4; [project bridge](PRESKILL_BRIDGE.md#limits); [scientific account](../science/capacity_reduction.md).

<a id="m14"></a>
### M14 — The complete resource comparison

**Phase:** Background/preliminaries.

**Central question:** What is shared between the three detector classes?

**Understanding target:** Reconstruct the same splitter, mean signal budget, unconditional criterion, and arbitrary endpoint coding for counting, individual-mode, and collective helpers.

**Dependencies:** [M03](#m03), [M05](#m05), [M06](#m06), [M11](#m11), [M12](#m12), [M13](#m13).

**Story role:** Synthesize the background into the exact research question.

**Conceptual connection:** Restricting helper processing does not restrict sender or receiver block coding.

**Sources:** Preskill §§10.7.1–10.7.3; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific account](../science/model.md).

## Narrative and innovation — M15–M30

<a id="m15"></a>
### M15 — Joint output degradation

**Phase:** Narrative/innovation.

**Central question:** Why does the same attenuation map work after a helper outcome?

**Understanding target:** Follow the helper-preserving channel identity, including arbitrary references, and distinguish its proof from a check on output populations.

**Dependencies:** [M14](#m14).

**Story role:** Begin the research argument with its shared operational mechanism.

**Conceptual connection:** An identity before the helper measurement passes through a filter on the untouched helper register.

**Sources:** Preskill §§10.7.3; [project bridge](PRESKILL_BRIDGE.md#degradation); [scientific account](../science/capacity_reduction.md).

<a id="m16"></a>
### M16 — The inherited collective benchmark

**Phase:** Narrative/innovation.

**Central question:** How is the best collective rate fixed without assuming Gaussian inputs?

**Understanding target:** Combine the arbitrary-encoder converse, thermal-reference contraction, and attributed assistance construction; identify this capacity as inherited.

**Dependencies:** [M09](#m09), [M13](#m13), [M15](#m15).

**Story role:** Set the benchmark against which detector restrictions are measured.

**Conceptual connection:** A thermal construction attains a converse that permits correlated and non-Gaussian input codes.

**Sources:** Preskill §§10.2.4–10.2.5; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#degradation); [scientific account](../science/capacity_reduction.md).

<a id="m17"></a>
### M17 — The all-input counting reduction

**Phase:** Narrative/innovation.

**Central question:** Why may the counting optimization use number distributions?

**Understanding target:** Explain phase averaging, concavity, degradability, and the difference H(J|K)−H(W|K), without restricting the transmitted messages to classical number states.

**Dependencies:** [M07](#m07), [M11](#m11), [M12](#m12), [M15](#m15).

**Story role:** Convert the optical counting capacity into the right variational problem.

**Conceptual connection:** A diagonal average state is compatible with quantum codewords and a purifying reference.

**Sources:** Preskill §§10.2.2; 10.7.3; [project bridge](PRESKILL_BRIDGE.md#counting-example); [scientific account](../science/capacity_reduction.md).

<a id="m18"></a>
### M18 — A variance bound that survives rare pulses

**Phase:** Narrative/innovation.

**Central question:** How can a mean budget control uncertainty without a finite input variance?

**Understanding target:** Derive the residual J−aK/c, use its conditional second moment, and connect the integer entropy bound to the energy-only half logarithm.

**Dependencies:** [M02](#m02), [M07](#m07), [M17](#m17).

**Story role:** Establish the first universal counting converse.

**Conceptual connection:** Canceling the conditional mean before averaging avoids an unsupported bound on the original photon-number variance.

**Sources:** Preskill §§10.1.1–10.1.2; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific account](../science/counting_bounds.md).

<a id="m19"></a>
### M19 — Thinning exposes inaccessible loss

**Phase:** Narrative/innovation.

**Central question:** How does the counting entropy difference become a difference of thinning information?

**Understanding target:** Follow the sufficient count sums and binomial entropy terms in the exact thinning identity.

**Dependencies:** [M07](#m07), [M10](#m10), [M17](#m17).

**Story role:** Find a converse controlled by inaccessible loss rather than incident power.

**Conceptual connection:** The same multinomial triple appears in two conditional entropy ledgers, allowing its conditional entropy to cancel.

**Sources:** Preskill §§10.1.2; 10.1.4; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific account](../science/counting_bounds.md).

<a id="m20"></a>
### M20 — A uniform loss-dependent counting ceiling

**Phase:** Narrative/innovation.

**Central question:** Why does the thinning identity bound every finite-mean input?

**Understanding target:** Connect thinning row sums to entropy gain and binomial collision estimates to the loss-dependent plateau bound.

**Dependencies:** [M08](#m08), [M10](#m10), [M19](#m19).

**Story role:** Complete the second counting converse.

**Conceptual connection:** The bound is uniform in the input law and is not an asymptotic expansion for one preferred distribution.

**Sources:** Preskill §§10.1.4; 10.2.1; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific account](../science/counting_bounds.md).

<a id="m21"></a>
### M21 — The counting construction

**Phase:** Narrative/innovation.

**Central question:** Which allowed input supplies the matching logarithmic order?

**Understanding target:** Derive the conditional negative-binomial law from a thermal average input and explain its collision-entropy and geometric-tail estimates.

**Dependencies:** [M07](#m07), [M08](#m08), [M09](#m09), [M13](#m13), [M17](#m17).

**Story role:** Supply an operational lower bound rather than infer tightness from a converse.

**Conceptual connection:** Using a thermal input for achievability does not claim it is the exact finite-energy optimizer.

**Sources:** Preskill §§10.1.2; 10.2.5; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific account](../science/counting_bounds.md).

<a id="m22"></a>
### M22 — The half-logarithmic counting law

**Phase:** Narrative/innovation.

**Central question:** How do the energy and loss bounds join uniformly?

**Understanding target:** Choose the allowed construction energy min(E,1/b), combine both converses, and track which constants depend only on the fixed received fraction.

**Dependencies:** [M18](#m18), [M20](#m20), [M21](#m21).

**Story role:** Synthesize the counting branch of the proof.

**Conceptual connection:** A minimum of two physical resource scales controls both the achievable and converse logarithms.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#limits); [scientific account](../science/uniform_laws.md).

<a id="m23"></a>
### M23 — A complete coherent measurement on one mode

**Phase:** Narrative/innovation.

**Central question:** What physical POVM replaces counting?

**Understanding target:** Verify the finite fourth-root-phase effects, their sum, the full-Fock-space completion, and the absence of postselection.

**Dependencies:** [M05](#m05), [M08](#m08), [M13](#m13), [M14](#m14).

**Story role:** Start the contrasting constructive detector argument.

**Conceptual connection:** Coherent control over number levels within one mode does not require quantum memory between collected modes.

**Sources:** Preskill §§10.2.2; 10.6.1; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m24"></a>
### M24 — The phase-averaged purity identity

**Phase:** Narrative/innovation.

**Central question:** Why do fourth-root phases leave only the needed pairings?

**Understanding target:** Track the block indices, the two surviving pairings, and the diagonal subtraction term; explain why independent signs are not equivalent.

**Dependencies:** [M08](#m08), [M23](#m23).

**Story role:** Expose the calculable mechanism behind the coherent detector.

**Conceptual connection:** A finite phase average converts many conditional quantum states into two marginal purities and a nonnegative correction.

**Sources:** Preskill §§10.9; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m25"></a>
### M25 — From purity to a one-mode rate

**Phase:** Narrative/innovation.

**Central question:** How does the finite phase measurement give a full-Fock-space guarantee?

**Understanding target:** Apply entropy versus purity, Jensen and concavity, then take the coded cutoff limit with thermal entropy tails and energy slack.

**Dependencies:** [M09](#m09), [M11](#m11), [M13](#m13), [M24](#m24).

**Story role:** Connect the construction to an actual achievable capacity lower bound.

**Conceptual connection:** The helper remains individual-mode even though the endpoints use long quantum codes.

**Sources:** Preskill §§10.7.1–10.7.2; 10.9.4; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m26"></a>
### M26 — The constant gap to collective assistance

**Phase:** Narrative/innovation.

**Central question:** Why can joint helper processing add at most a bounded rate?

**Understanding target:** Compare the purity lower bound with the collective entropy formula and verify the scalar log2(e) bound, including clipping a negative lower bound at zero.

**Dependencies:** [M16](#m16), [M25](#m25).

**Story role:** Quantify the residual value of cross-mode helper processing.

**Conceptual connection:** A lower bound suffices to prove proximity to an optimum without identifying the exact individual-mode optimum.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific account](../science/coherent_measurements.md).

<a id="m27"></a>
### M27 — The full energy–collection crossover

**Phase:** Narrative/innovation.

**Central question:** When is the factor-of-two statement valid?

**Understanding target:** Combine the counting and coherent laws with the fixed-a uniform domain; distinguish joint high-energy/low-loss paths from fixed-loss saturation.

**Dependencies:** [M22](#m22), [M26](#m26).

**Story role:** Join the two detector branches into the main theorem.

**Conceptual connection:** An asymptotic leading coefficient is not a universal finite-energy ratio.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#limits); [scientific account](../science/uniform_laws.md).

<a id="m28"></a>
### M28 — Finite certificates and their meaning

**Phase:** Narrative/innovation.

**Central question:** What does the finite-energy example certify?

**Understanding target:** Interpret the all-input counting upper bound, achieved coherent lower bound, and collective value; distinguish rational enclosures from measured device performance.

**Dependencies:** [M17](#m17), [M25](#m25), [M26](#m26), [M27](#m27).

**Story role:** Connect the general theorem to a reproducible finite separation.

**Conceptual connection:** A numerical certificate validates the evaluation of proved bounds, not the universal channel theorem by itself.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#counting-example); [scientific account](../science/uniform_laws.md).

<a id="m29"></a>
### M29 — The physical resource distinction

**Phase:** Narrative/innovation.

**Central question:** Which coherence is useful, and what remains unpriced?

**Understanding target:** Distinguish within-mode coherence, cross-mode control, endpoint coding, phase references, and classical postprocessing; state the construction’s implementation limits.

**Dependencies:** [M14](#m14), [M23](#m23), [M27](#m27), [M28](#m28).

**Story role:** Translate the theorem back to the physical apparatus.

**Conceptual connection:** Photon counting is already non-Gaussian, so Gaussianity is not the resource distinction proved here.

**Sources:** Preskill §§10.2.2; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific account](../science/interpretation.md).

<a id="m30"></a>
### M30 — The complete scientific story

**Phase:** Narrative/innovation.

**Central question:** What has been established beyond the inherited benchmark?

**Understanding target:** Explain the model, both detector mechanisms, uniform laws, constant gap, finite certificate, source attribution, and decisive boundaries as one connected argument.

**Dependencies:** [M16](#m16), [M22](#m22), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29).

**Story role:** Finish with the complete contribution and its evidence boundaries.

**Conceptual connection:** Separate textbook foundations, inherited research results, local derivations, and still-unoptimized implementation resources.

**Sources:** Preskill §§10.10; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific account](../science/README.md).
