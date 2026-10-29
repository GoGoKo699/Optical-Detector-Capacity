# Learn optical detector capacity

[Home](../README.md) · [Thirty milestones](MILESTONES.md) · [Preskill bridge](PRESKILL_BRIDGE.md) · [Scientific route](../science/README.md)

A receiver obtains part of an optical signal, while a helper measures some of the lost light and sends its classical record to the receiver. Why can counting lose half the leading quantum transmission rate, whereas a coherent measurement on each mode retains it? Once that distinction is understood, the apparatus question follows: how many prepared reference photons are needed for the coherent advantage?

## One source and a project-specific bridge

The single educational anchor is **John Preskill, *Quantum Shannon Theory*, Chapter 10**, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5). The draft states **updated June 2025**; the version was posted **8 July 2025**. Use this pinned version for the section and page references in the bridge. The chapter is linked, not redistributed.

Begin with the bridge's [source map and notation](PRESKILL_BRIDGE.md#sources), then its [worked counting example](PRESKILL_BRIDGE.md#counting-example). The [milestone map](MILESTONES.md) supplies a connected route: M01–M14 assemble the background and resource model, M15–M25 establish the detector comparison, and M26–M30 connect finite apparatus resources to the complete mean-reference capacity profile. Source pointers select relevant sections rather than assign the entire chapter.

Preskill supplies the entropy and coding foundations. The bridge adds the optical calculation, detector mechanisms, finite reference, and local-conservation arguments. The [science pages](../science/README.md) contain the exact statements and proofs. Primary papers remain necessary for assistance, energy-constrained coding, phase designs, and reference implementations; they are not additional educational anchors.

## Reading routes

For the physical story, follow the bridge from [optical systems](PRESKILL_BRIDGE.md#optics) through the [detector mechanism](PRESKILL_BRIDGE.md#coherence), [finite reference](PRESKILL_BRIDGE.md#phase-reference), and [capacity profile](PRESKILL_BRIDGE.md#local-reference). Use the corresponding milestones to connect each step.

For the exact proofs, the [scientific route](../science/README.md) connects the base channel comparison to the record, finite-reference, width, and mean-budget extensions. Read their contracts before transferring a conclusion between them. Use the bridge when a prerequisite or convention needs unpacking.

Keep the registers and budgets explicit. The logical reference $`R`$ tests transmission; the apparatus reference $`W`$ supplies photon-number coherence and may be discarded. Individual-mode helper processing still permits arbitrary endpoint block codes. The signal mean $`E`$, reference mean $`M`$, and classical record cost are separate resources.

<a id="reproduce-the-learning-checks"></a>
## Reproduce the learning checks

After installing the [verification dependency](../verification/requirements.txt), run from the repository root:

```bash
python verification/check_learning.py
python -m unittest discover -s verification -p "test_learning.py" -v
python verification/verify.py
```

The structural checker verifies all thirty IDs, the 14/16 phase allocation, earlier dependencies, required fields, local links, and the selected source version. The tests cover the worked counting calculation, measurement operators, thermal identities, and failure detection in the structural checker. The [scientific verification route](../verification/README.md) adds the actual finite-reference channels and resource converses. These checks do not establish hosted visual rendering, a coding theorem, or experimental performance.
