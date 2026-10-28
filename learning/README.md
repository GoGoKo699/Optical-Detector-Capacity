# Learn optical detector capacity

[Home](../README.md) · [Thirty milestones](MILESTONES.md) · [Preskill bridge](PRESKILL_BRIDGE.md) · [Scientific route](../science/README.md)

A receiver obtains part of an optical signal, while a helper measures some of the lost light. Both parties may retain the entire classical measurement record. Why can counting that light lose half the leading quantum transmission rate, whereas another measurement on each individual mode does not?

## One source and a project-specific bridge

The single educational anchor is **John Preskill, *Quantum Shannon Theory*, Chapter 10**, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5). The draft states **updated June 2025**; the version was posted **8 July 2025**. Use this pinned version for the section and page references in the bridge. The chapter is linked, not redistributed.

Begin with the bridge's [source map and notation](PRESKILL_BRIDGE.md#sources), then its [worked counting example](PRESKILL_BRIDGE.md#counting-example). The [milestone map](MILESTONES.md) supplies a connected route through the whole project: M01–M14 assemble the background and resource model; M15–M30 develop and interpret the detector comparison. Source pointers select relevant sections rather than assign the entire chapter.

Preskill supplies the entropy and coding foundations. The bridge adds the optical model, conditional counting calculation, oscillator energy formulas, and explanations of the research mechanisms. The [science pages](../science/README.md) contain the exact statements and proofs. Primary papers remain necessary for research attribution and the energy-constrained coding theorem; they are not additional educational anchors.

## Reading routes

For the physical story, follow the bridge from [optical systems](PRESKILL_BRIDGE.md#optics) through [the final comparison](PRESKILL_BRIDGE.md#synthesis), using the corresponding milestones to connect each step.

For a proof-oriented route, read the [model](../science/model.md), [all-code reduction](../science/capacity_reduction.md), [counting bounds](../science/counting_bounds.md), [coherent measurement](../science/coherent_measurements.md), and [uniform laws](../science/uniform_laws.md). Use the bridge when a prerequisite or convention needs unpacking.

Keep three distinctions visible throughout: a classical outcome is not a coherent helper link; a diagonal average input does not force classical messages; and individual-mode helper processing does not mean individual-mode endpoint coding.

<a id="reproduce-the-learning-checks"></a>
## Reproduce the learning checks

After installing the [verification dependency](../verification/requirements.txt), run from the repository root:

```bash
python verification/check_learning.py
python -m unittest discover -s verification -p "test_learning.py" -v
python verification/verify.py
```

The structural checker verifies all thirty IDs, the 14/16 phase allocation, earlier dependencies, required fields, local links in the learning documents and README, and the selected source version. The tests cover the worked counting calculation, measurement operators, thermal identities, and failure detection in the structural checker. The original scientific suite and reference output remain unchanged. These checks do not establish hosted visual rendering, a coding theorem, or experimental performance.
