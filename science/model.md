# Physical task, resources, and claims

[Home](../README.md) · [Proof route](README.md)

## One signal, three outputs

A memoryless passive splitter has vacuum at its unused inputs. For nonnegative $`a,b,c`$ with $`a+b+c=1`$, its isometry is

```math
V|n\rangle_A=
\sum_{j+w+k=n}\sqrt{\frac{n!}{j!w!k!}}
 a^{j/2}b^{w/2}c^{k/2}|j\rangle_B|w\rangle_Z|k\rangle_D.
```

The receiver holds $`B`$, $`Z`$ is inaccessible, and a helper holds $`D`$. The alternate notation $`a=\eta`$, $`b=u`$ identifies received and inaccessible fractions. All fractions refer to the original signal; collection has already occurred before any helper processing.

The input and outputs are ordinary oscillator Fock spaces, and states are normal trace-class states. Operations are normal quantum channels or instruments. Classical outcome spaces may be finite, countable, or standard Borel; continuous records are interpreted by conditional states, not differential-entropy subtraction.

## Communication and energy

An $`n`$-use code transmits one half of a maximally entangled logical state of dimension $`d_n`$. Arbitrary encoding and receiver decoding are allowed. If $`\rho_{A^n}`$ is the encoded state averaged over the logical input, the constraint is

```math
\mathrm{Tr}\!\left(\rho_{A^n}\sum_{i=1}^n\hat n_i\right)\le nE.
```

The rate is $`\liminf n^{-1}\log_2d_n`$ with unconditional entanglement fidelity tending to one. All trials and measurement outcomes count. The constraint is on mean signal photons, averaged over the message and uses, not peak photon number, second moment, or the energy of every branch. Encoder ancillas may be discarded; the converse includes them.

There is no initial shared entanglement, coherent helper link, sender feedback, or additional sender–receiver classical channel. The helper sends an unlimited reliable classical record to the receiver only. Endpoint quantum memory and coding complexity are unrestricted. Device preparation, a phase reference, and detector-control energy are not charged to $`E`$.

The [reference-resource extensions](reference_mean_bounds.md) separately charge
initial mean reference photons $`M`$, keeping the signal constraint $`E`$.
Their operation contract requires helper effects to commute with every local
signal-plus-reference number, and reference initialization independent of the
encoded signal. Mean stock, support width, gate accuracy, preparation work, and
reset are distinct resources. The mean-stock and width profiles use unrestricted
classical records; the [record-budget result](detector_resources.md) is a
separate optimization.

## Three detector classes

**Counting, $`Q_{\rm cnt}`$.** Each collected mode is measured in its number basis. The receiver can retain and process the complete vector of counts. Any stochastic processing, coarse graining, or diagonal POVM on the product number basis is dominated by this exact record. A coherent optical transformation before counting changes the detector class and is not included in this benchmark.

**Individual-mode processing, $`Q_1`$.** Each mode has an arbitrary POVM chosen in advance. The choice may vary with the use, the known channel parameters, energy budget, and desired accuracy; time sharing is allowed. No joint quantum operation or persistent quantum memory connects collected modes. The sender and receiver still use arbitrary block codes. An exact single-letter formula for this optimized class is not asserted or needed.

**Collective processing, $`Q_{\rm coll}`$.** The helper may jointly measure all collected modes of a block. It still communicates only classically to the receiver. These definitions imply

```math
0\le Q_{\rm cnt}(E)\le Q_1(E)\le Q_{\rm coll}(E).
```

Adaptive choices of single-mode measurements are not needed for the lower bound. Their capacity lies between $`Q_1`$ and $`Q_{\rm coll}`$, so it inherits the same leading law and constant-gap upper comparison without an exact characterization.

## Entropy and notation

All logarithms and entropies are in bits unless $`\ln`$ is written. Put

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,\qquad g(0)=0.
```

This is the entropy of a thermal oscillator with mean occupation $`x`$. A thermal state used below is an average coded input, not a claim that an uncoded thermal signal carries quantum information.

In the classical reduction, $`N`$ is input photon number, $`J`$ the received count, $`K`$ the collected count, and $`W`$ the inaccessible count. Conditional on $`N=n`$, they are multinomial with probabilities $`a,c,b`$, respectively. $`T_tN`$ denotes independent binomial thinning with retention $`t`$.

## Main claims

The inherited collective capacity is

```math
Q_{\rm coll}(E)=
\begin{cases}g(aE)-g(bE),&a>b,\\0,&a\le b.\end{cases}
```

The [operational proof](capacity_reduction.md) states its origin and covers arbitrary codes. For $`a>b`$, the [coherent construction](coherent_measurements.md) proves

```math
Q_1(E)\ge
\max\!\left\{0,-\log_2\!\left[
\frac1{1+2aE}+\frac1{1+2(1-b)E}\right]-g(bE)\right\}.
```

Consequently $`0\le Q_{\rm coll}-Q_1\le\log_2e`$ for every finite energy. All three capacities vanish when $`a\le b`$.

For fixed $`0\lt a\lt 1`$, let $`b_0=\frac12\min\{a,1-a\}`$. Uniformly over $`E\ge1`$ and $`0\le b\le b_0`$, with $`L=\min\{E,1/b\}`$ and $`1/0=\infty`$,

```math
Q_{\rm cnt}(E)=\frac12\log_2L+O_a(1),
\qquad Q_1(E)=Q_{\rm coll}(E)+O(1)=\log_2L+O_a(1).
```

The [finite counting bounds](counting_bounds.md) establish both sides without a peak constraint. The constants may depend on the fixed received fraction, not on $`E`$ or $`b`$. The leading-factor comparison concerns $`L\to\infty`$, not a fixed-loss energy limit. [Boundary cases and the finite comparison](uniform_laws.md) complete the statement.
