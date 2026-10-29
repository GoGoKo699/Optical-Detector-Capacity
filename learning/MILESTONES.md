# Thirty-milestone understanding map

[Home](../README.md) · [Learning entrance](README.md) · [Preskill bridge](PRESKILL_BRIDGE.md) · [Scientific route](../science/README.md)

The map has **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. The background joins optical carriers, classical records, entropy, and coding into one resource model. The narrative develops the detector comparison, then follows the finite apparatus through a matched mean-reference capacity profile. The allocation follows that scientific structure, not a particular reader's preparation.

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

**Understanding target:** Identify the receiver flag and its complementary copy after a rank-one measurement, and retain unresolved helper or discarded apparatus systems when the detector changes.

**Dependencies:** [M04](#m04), [M05](#m05).

**Story role:** Prevent an incomplete environmental entropy ledger.

**Conceptual connection:** The inaccessible optical mode alone is not generally the complement; a discarded phase reference can carry additional information.

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
### M19 — The loss-dependent counting ceiling

**Phase:** Narrative/innovation.

**Central question:** How does inaccessible loss limit counting at arbitrarily large input energy?

**Understanding target:** Follow the thinning identity, its row-sum entropy bound, and the binomial collision estimate; explain why the resulting ceiling permits every finite-mean input.

**Dependencies:** [M07](#m07), [M08](#m08), [M10](#m10), [M17](#m17).

**Story role:** Add the loss-dependent converse to the energy-only bound.

**Conceptual connection:** Sufficient count sums reveal an entropy cancellation; the remaining estimate is uniform in the input law.

**Sources:** Preskill §§10.1.2; 10.1.4; 10.2.1; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific account](../science/counting_bounds.md).

<a id="m20"></a>
### M20 — The matching counting construction

**Phase:** Narrative/innovation.

**Central question:** Which allowed input attains the half-logarithmic order?

**Understanding target:** Derive the conditional negative-binomial law for a thermal average input, use its collision and logarithmic-moment estimates, and combine both converses at energy min(E,1/b).

**Dependencies:** [M09](#m09), [M13](#m13), [M17](#m17), [M18](#m18), [M19](#m19).

**Story role:** Complete the counting branch with a matching achievable rate.

**Conceptual connection:** A thermal construction establishes the leading order without identifying the exact finite-energy optimizer.

**Sources:** Preskill §§10.1.2; 10.2.5; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#counting-mechanism); [scientific accounts](../science/counting_bounds.md), [uniform domain](../science/uniform_laws.md).

<a id="m21"></a>
### M21 — A complete coherent measurement on one mode

**Phase:** Narrative/innovation.

**Central question:** What measurement changes the useful photon-number coherence?

**Understanding target:** Verify the finite phase effects and full-space completion, and explain why classical processing after counting cannot reproduce coherent superposition of measurement branches.

**Dependencies:** [M05](#m05), [M08](#m08), [M13](#m13), [M14](#m14).

**Story role:** Begin the constructive detector argument.

**Conceptual connection:** Coherent control within one oscillator differs from joint quantum processing of collected modes.

**Sources:** Preskill §§10.2.2; 10.6.1; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m22"></a>
### M22 — Purity moments and one selected Fourier setting

**Phase:** Narrative/innovation.

**Central question:** Why can a structured finite detector replace the independent phase family?

**Understanding target:** Track the two fourth-moment pairings and diagonal subtraction, reproduce them with the inherited quadratic-phase design, and select a fixed setting with linearly many outcomes.

**Dependencies:** [M08](#m08), [M21](#m21).

**Story role:** Turn a computable phase average into a specified detector.

**Conceptual connection:** Universal moment reproduction and existence of one useful measurement have different outcome-count requirements.

**Sources:** Preskill §§10.9; [project bridge](PRESKILL_BRIDGE.md#coherence); [scientific account](../science/coherent_measurements.md).

<a id="m23"></a>
### M23 — From purity to an achievable optical rate

**Phase:** Narrative/innovation.

**Central question:** How does a finite detector yield a full-Fock-space rate guarantee?

**Understanding target:** Apply entropy versus purity and concavity, evaluate the thermal marginals, and take the coding limit before the cutoff limit while retaining strict mean-energy slack.

**Dependencies:** [M09](#m09), [M11](#m11), [M13](#m13), [M22](#m22).

**Story role:** Establish the individual-mode capacity lower bound.

**Conceptual connection:** The chosen finite support enables achievability without imposing a peak constraint on the converse.

**Sources:** Preskill §§10.7.1–10.7.2; 10.9.4; [project bridge](PRESKILL_BRIDGE.md#limits); [scientific account](../science/coherent_measurements.md).

<a id="m24"></a>
### M24 — The constant gap and uniform detector comparison

**Phase:** Narrative/innovation.

**Central question:** How close is individual-mode detection to collective assistance?

**Understanding target:** Compare the coherent lower bound with the inherited collective formula, obtain the log2(e) finite-energy gap, and join the counting and coherent laws in the fixed-a uniform domain.

**Dependencies:** [M16](#m16), [M20](#m20), [M23](#m23).

**Story role:** Assemble the main detector-class theorem.

**Conceptual connection:** A bounded additive gap gives the same leading rate without proving an exact individual-mode optimum; fixed-loss saturation is a different limit.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific accounts](../science/coherent_measurements.md), [uniform laws](../science/uniform_laws.md).

<a id="m25"></a>
### M25 — Two finite separations and their input classes

**Phase:** Narrative/innovation.

**Central question:** What do the numerical certificates actually separate?

**Understanding target:** Distinguish the unrestricted mean-energy optical certificate from the two-photon-cutoff example; explain the global counting upper bounds, coherent achievable rates, and role of rational enclosures.

**Dependencies:** [M17](#m17), [M21](#m21), [M23](#m23), [M24](#m24).

**Story role:** Connect the universal comparison to finite, reproducible witnesses.

**Conceptual connection:** Vacuum/one-photon counting optimality is compatible with a two-photon counterexample and an unbounded full-oscillator disadvantage.

**Sources:** Preskill §§10.7.1; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific accounts](../science/qubit_optical_bridge.md), [finite optical certificate](../science/uniform_laws.md).

<a id="m26"></a>
### M26 — Cutoff, classical record, and control accuracy

**Phase:** Narrative/innovation.

**Central question:** Which finite detector resources suffice for a specified rate gap?

**Understanding target:** Connect thermal tail mass to cutoff size, count the complete transmitted record, and interpret the continuity bound through the actual receiver and logical-reference state.

**Dependencies:** [M06](#m06), [M13](#m13), [M22](#m22), [M24](#m24).

**Story role:** Make the abstract coherent detector's finite requirements explicit.

**Conceptual connection:** A logarithmic record requirement, a finite accuracy guarantee, and a physical synthesis cost are different statements.

**Sources:** Preskill §§10.6.1–10.6.3; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#record-resources); [scientific account](../science/detector_resources.md).

<a id="m27"></a>
### M27 — A finite phase reference and conserving control

**Phase:** Narrative/innovation.

**Central question:** How can a detector mix photon numbers while conserving total excitation?

**Understanding target:** Follow the finite sine reference and total-number-sector lift, identify the reference shifts, and distinguish the initial photon stock from the net photons transferred during control.

**Dependencies:** [M02](#m02), [M05](#m05), [M14](#m14), [M22](#m22), [M26](#m26).

**Story role:** Supply an explicit finite apparatus for the prescribed coherent detector.

**Conceptual connection:** Gate approximation can be realized with a finite reference that becomes correlated or changes after use; exact return is a separate demand.

**Sources:** Preskill §§10.2.5; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#phase-reference); [scientific account](../science/finite_reference.md).

<a id="m28"></a>
### M28 — Pay the discarded-reference entropy directly

**Phase:** Narrative/innovation.

**Central question:** Why does communication need less than a shrinking uniform gate error?

**Understanding target:** Retain the actual ZW complement, bound the entropy of conditional translated sine references, and combine this with receiver entropy concavity to obtain a linear sufficient reference mean.

**Dependencies:** [M06](#m06), [M08](#m08), [M09](#m09), [M23](#m23), [M27](#m27).

**Story role:** Turn the finite apparatus into a communication-specific resource bound.

**Conceptual connection:** Maximum-entropy reasoning can bound discarded information using an auxiliary Laplacian mode number without identifying it with physical photon energy.

**Sources:** Preskill §§10.2.2–10.2.5; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#phase-reference); [scientific account](../science/direct_reference.md).

<a id="m29"></a>
### M29 — Separate local invariance and all-code resource converses

**Phase:** Narrative/innovation.

**Central question:** What operation constraint makes reference spread and mean stock necessary?

**Understanding target:** Refine the record by each local conserved total, bound logical coherent information by conditional number entropy, and distinguish the variance/width estimate from the first-absolute-moment mean-energy bound.

**Dependencies:** [M02](#m02), [M07](#m07), [M10](#m10), [M18](#m18), [M27](#m27).

**Story role:** Supply converses for every allowed code rather than only the constructed detector.

**Conceptual connection:** Large variance at fixed mean defeats a variance-to-mean inference; the mean converse instead permits infinite variance directly. Global conservation alone is a broader operation class.

**Sources:** Preskill §§10.1.1–10.1.2; 10.2.2; 10.7.1; [project bridge](PRESKILL_BRIDGE.md#local-reference); [scientific accounts](../science/reference_width_bounds.md), [mean-energy converse](../science/reference_mean_bounds.md).

<a id="m30"></a>
### M30 — The complete detector and mean-reference capacity story

**Phase:** Narrative/innovation.

**Central question:** How do detector choice and a charged phase-reference budget determine the rate?

**Understanding target:** Combine counting, the direct finite-reference construction, and the all-code mean converse into the additive capacity profile; state its energy-driven domain, bounded-gap requirement, attribution, and remaining implementation limits.

**Dependencies:** [M16](#m16), [M20](#m20), [M24](#m24), [M25](#m25), [M26](#m26), [M28](#m28), [M29](#m29).

**Story role:** Finish with the connected scientific contribution and its operational boundaries.

**Conceptual connection:** Linear mean reference stock is sufficient and necessary for a bounded gap under separate local invariance; neither the profile nor the record theorem determines a joint resource frontier or preparation work.

**Sources:** Preskill §§10.10; [project bridge](PRESKILL_BRIDGE.md#synthesis); [scientific accounts](../science/reference_mean_bounds.md), [proof route](../science/README.md).
