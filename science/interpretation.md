# What the detector comparison means

[Home](../README.md) · [Model](model.md) · [Uniform result](uniform_laws.md)

## Counting keeps a number record, not all useful coherence

The received field and collected field share photon-number fluctuations. A count of the collected light estimates the original occupation, and the residual uncertainty has a square-root scale. The energy converse turns that intuition into an all-input bound through $`J-aK/c`$: its second moment depends only on mean input energy. A rare high-photon pulse cannot evade it by giving the original distribution a very large variance.

A coherent detector measures superpositions of different collected photon numbers. Its record does not first distinguish those alternatives and then forget them. The distinction is physical: classical coarse graining after a number measurement cannot undo its backaction. The finite phase POVM demonstrates that the remaining receiver entropy can instead grow with the full logarithmic scale.

## Two different meanings of collective quantum control

The coherent construction needs control across Fock levels of one oscillator. It does not need a joint operation across the collected modes from different channel uses. These are different resources. The receiver and sender still require arbitrary quantum block coding in both comparisons. The theorem does not replace the full communication system with independent single-mode encoders and decoders.

The measured mode is converted into a classical outcome; no helper quantum state reaches the receiver. Conversely, unrestricted classical processing of all exact count records is already allowed to the counting benchmark. Its lower performance is not caused by restricting classical computation or hiding count records.

## Relation to the qubit result

The earlier partial-monitoring project proves that counting is optimal over predetermined product helper POVMs for its vacuum/one-excitation qubit input. It explicitly does not extend that optimization to the full oscillator. Here the number of occupied photon levels can grow. The two results therefore describe different input models: qubit counting optimality and an unbounded optical disadvantage are compatible.

The earlier collective optical capacity is reused and attributed once. Environmental assistance, coherent superpositions of assistance outcomes, degradability, and energy-constrained coding are established methods. The present operational comparison is specified in [Related work](../references/RELATED_WORK.md), rather than claimed through a new name for those methods.

## Costs and scope

The energy parameter counts incident signal photons. A phase reference and general coherent detector control are supplied, and their energy and gate complexity are not optimized. The explicit fourth-root-phase POVM has exponentially many outcomes in its Fock cutoff; it proves existence, not practical hardware efficiency. A simpler detector attaining the same law would be an additional implementation result.

The baseline is number-diagonal measurement in the original collected-mode basis. A coherent multimode interferometer followed by counting, a nonlinear preprocessor, or coherent delivery of the collected field changes that access model. The result does not impose the counting ceiling on those resources.

Photon counting is itself a non-Gaussian measurement. The separation is therefore not a no-go theorem for Gaussian measurements or a generic claim that non-Gaussian operations suffice. The constructed coherent POVM is one successful family; optimal Gaussian-helper capacity is not established here.

Vacuum auxiliary inputs, memoryless loss, accurate known fractions, unconditional transmission, and receiver-only classical assistance are consequential premises. Thermal background noise, a drifting phase reference, finite classical bandwidth, finite-block fidelity, and physical detector synthesis require separate analyses. No claim about their behavior is needed for the stated capacity theorem.
