# From quantum Shannon theory to optical detector capacity

[Learning entrance](README.md) · [Thirty milestones](MILESTONES.md) · [Exact model](../science/model.md) · [Proof route](../science/README.md)

The project compares three ways of reading collected light while keeping the same signal channel and endpoint coding resources. It then charges the finite phase reference used by a coherent detector. This bridge connects the optical mechanisms and apparatus constraints to entropy and channel coding. The exact proofs remain in `science/`.

<a id="sources"></a>
## Source and focused reading map

**John Preskill, *Quantum Shannon Theory*, Chapter 10, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5).** The title page says updated June 2025; arXiv posted this version on 8 July 2025. Page numbers below are the chapter's printed Arabic pages, not the PDF viewer's page count. The source is linked, not copied into the repository.

| Sections in the pinned chapter | Printed pages | Use here |
|---|---:|---|
| 10.1.1–10.1.2; 10.1.4 | 2–8 | Classical entropy, conditioning, and information comparisons |
| 10.2.1–10.2.4 | 15–20 | Quantum entropy inequalities and processing of correlations |
| 10.2.5 | 20–21 | Energy and maximum-entropy reasoning |
| 10.6.1–10.6.3 | 40–43 | Measurement outcomes and retained classical information |
| 10.7.1–10.7.2 | 51–56 | Quantum rates, coherent information, and preservation of a reference |
| 10.7.3 | 56–58 | Complementary channels, degradation, and additivity |
| 10.9; 10.9.4 | 68–76 | Optional second-moment and coding perspective |
| 10.10 | 78–79 | Background synthesis after working through the project |

The optical counting converses, phase POVM, constant-gap comparison, and reference-resource profiles are additional arguments. They are not results attributed to the chapter. The precise infinite-dimensional coding ingredient is the Wilde–Qi theorem; the phase designs and conserving reference constructions also retain their primary attributions in [Related work](../references/RELATED_WORK.md). Preskill remains the single educational anchor.

<a id="notation"></a>
## Translate notation before using a capacity formula

Preskill often writes quantum entropy as $`H(\rho)`$; this project writes $`S(\rho)`$ and reserves $`H`$ for classical distributions. Both use bits. The reference system is $`R`$; a transmission rate should not be confused with that register.

The chapter's environmental register $`E`$ becomes $`Z`$ for the inaccessible optical output here. Our scalar $`E`$ means the mean incident photon budget. After a helper measurement, the true complementary output is generally larger than $`Z`$.

Most importantly, Preskill's $`Q_1(\mathcal N)`$ in §10.7.1 is an optimized one-use coherent-information quantity for a fixed channel. Here $`Q_1(E)`$ means an **asymptotic capacity with individual-mode helper measurements**. Its sender and receiver may use arbitrary block codes. These are different definitions despite the shared subscript. The project does not claim an exact one-use formula for its optimized $`Q_1(E)`$.

Use $`d`$ for the photon cutoff dimension, with occupied levels $`0,\ldots,d-1`$, and $`d_n`$ for the transmitted logical dimension over $`n`$ uses. Neither generally equals the number of helper outcomes. Below, $`M`$ denotes mean reference photons and $`K_{\rm ref}`$ denotes reference support width. The apparatus reference $`W`$ is different from the logical reference $`R`$ whose entanglement tests transmission.

<a id="optics"></a>
## From one oscillator to the resource model

One optical mode has number states $`|n\rangle`$ for $`n=0,1,\ldots`$, with number operator $`\hat n|n\rangle=n|n\rangle`$. A state $`\rho`$ can have coherences between different number states. Its mean occupation is $`\mathrm{Tr}(\rho\hat n)`$.

For one photon, the splitter is particularly simple:

```math
V|0\rangle=|000\rangle_{BZD},
\qquad
V|1\rangle=\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle,
\qquad a+b+c=1.
```

The receiver holds $`B`$, the helper holds $`D`$, and no party can act on $`Z`$. For an input with $`n`$ photons, the number probabilities are multinomial. The isometry acts linearly on superpositions as well; replacing it by a classical random split would lose the quantum communication problem.

The energy constraint on a block is

```math
\mathrm{Tr}\!\left(\rho_{A^n}\sum_{i=1}^{n}\hat n_i\right)\le nE.
```

It prices the average coded signal, not its largest photon number. For example, a number distribution with probability $`2/m`$ at $`m\ge2`$ and the remaining probability at zero has mean two but second moment $`2m`$. It is allowed at budget two no matter how large $`m`$ becomes. This is why a converse cannot silently assume bounded variance. Reference photons are priced separately in the [local-conservation extension](../science/reference_mean_bounds.md); preparation work, reset, and endpoint circuit complexity remain outside that account.

<a id="flags"></a>
## The helper record belongs in the channel and its complement

For a rank-one helper measurement, let $`W_x:A\to BZ`$ be the unnormalized branch operator. A dilation of the measured channel is

```math
U_M=\sum_x W_x\otimes|x\rangle_X|x\rangle_Y.
```

The receiver gets $`BX`$, and a complementary output is $`ZY`$. For a finite record, the block-diagonal entropy identities give

```math
\begin{aligned}
S(BX)&=H(p)+\sum_xp_xS(\rho_{B|x}),\\
S(ZY)&=H(p)+\sum_xp_xS(\rho_{Z|x}),\\
I_c(\rho,\mathcal N_M)&=\sum_xp_x
\left[S(\rho_{B|x})-S(\rho_{Z|x})\right].
\end{aligned}
```

The record entropy cancels because both outputs contain the same classical label. It is not permission to omit the record from the complement. A coarse measurement can leave an unresolved helper system there as well; a finite apparatus can leave a discarded phase reference. For continuous records, the proof uses conditional states and finite partitions rather than subtracting divergent differential entropies.

This applies Preskill's §10.7.1 channel language to the actual measured apparatus. The [operational reduction](../science/capacity_reduction.md) handles arbitrary encoders, unresolved outputs, and the energy constraint.

<a id="counting-example"></a>
## A complete small counting calculation

Take $`a=1/2`$, $`b=c=1/4`$, and the average input $`\rho_A=(|0\rangle\langle0|+|1\rangle\langle1|)/2`$. Its mean signal occupation is $`1/2`$. It can be purified with a qubit reference; it is not a declaration that messages are classical.

The helper sees one photon with probability $`1/8`$. In that branch both $`B`$ and $`Z`$ are vacuum. With probability $`7/8`$ it sees zero photons. In this branch, the receiver's excitation probability is $`2/7`$ and the inaccessible excitation probability is $`1/7`$. Thus, with binary entropy $`h_2`$,

```math
I_c=\frac78\left[h_2\!\left(\frac27\right)
-h_2\!\left(\frac17\right)\right]
=0.237516816236\ldots.
```

Every outcome has been retained; the zero-contribution branch has not been postselected away. This is coherent information for one specified average input and detector. Coding turns a suitable positive coherent information into an achievable rate, but this calculation alone is neither a capacity optimum nor a counting-versus-coherent separation. The project's finite separation instead uses an all-input counting upper bound and a distinct coherent achievable bound in [Uniform laws](../science/uniform_laws.md).

<a id="thermal"></a>
## Two oscillator formulas that make the rate bounds computable

A thermal mode of mean occupation $`x>0`$ has the geometric probabilities

```math
p_n=\frac1{1+x}\left(\frac{x}{1+x}\right)^n.
```

Substitute their logarithm into $`H(p)`$ and use $`\sum_nnp_n=x`$ to obtain

```math
S(\tau_x)=g(x)
=(x+1)\log_2(x+1)-x\log_2x.
```

The geometric series for $`\sum_np_n^2`$ gives the second identity

```math
\mathrm{Tr}(\tau_x^2)=\frac1{1+2x}.
```

At $`x=0`$ the state is vacuum, with entropy zero and purity one. A vacuum attenuator of retention $`t`$ sends $`\tau_x`$ to $`\tau_{tx}`$.

For any state with eigenvalues $`\lambda_i`$, Jensen's inequality yields

```math
S(\rho)=\sum_i\lambda_i[-\log_2\lambda_i]
\ge-\log_2\sum_i\lambda_i^2.
```

This turns a purity upper bound into an entropy lower bound. It does not replace entropy by purity as an equality. The coherent detector uses this direction for the receiver, and entropy concavity in the opposite role to upper-bound the average inaccessible entropy.

For a converse, the thermal reference has a logarithm affine in $`\hat n`$. At the same mean energy, relative entropy therefore measures the entropy shortfall from $`g(x)`$. This is the connection to the chapter's maximum-entropy reasoning; the all-input channel argument is supplied in the [capacity reduction](../science/capacity_reduction.md).

<a id="degradation"></a>
## The joint identity is stronger than simulating a marginal

For $`a\ge b`$ and $`a>0`$, attenuating the receiver by $`b/a`$ reproduces the inaccessible output **while preserving its correlations with the helper**:

```math
\mathcal N_{ZD}=(\mathcal L_{b/a}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

The equality holds as a channel, including arbitrary input references. A helper measurement acts on $`D`$, so it commutes with this simulation. A rank-one measured channel is consequently degradable with the copied flag included. Preskill's §10.7.3 explains why correlation contraction then prevents endpoint entanglement across uses from increasing a fixed channel's coherent-information maximum.

The full collective converse must also allow coarse records and discarded encoder ancillas. The science page proves that stronger statement. Together with the attributed assistance construction and thermal-reference bound, it gives the inherited benchmark $`Q_{\rm coll}(E)=g(aE)-g(bE)`$ when $`a>b`$. Reversing the joint simulation gives the zero-capacity side when $`a\le b`$. These are not conclusions obtained by ignoring $`D`$ or by comparing two marginal mean photon numbers.

<a id="counting-mechanism"></a>
## Why counting has only half the leading logarithm

Let $`J`$ be received count and $`K`$ collected count. For a fixed input number $`N=n`$, the residual $`J-aK/c`$ has conditional mean zero. The multinomial variance and covariance give, for $`c>0`$,

```math
\mathbb E\!\left[\left(J-\frac acK\right)^2\middle|N=n\right]
=\frac{a(a+c)}c\,n.
```

After averaging, only $`\mathbb EN`$ appears. Since the conditional mean estimator minimizes mean-square error, this also bounds the average conditional variance of $`J`$ given $`K`$. An integer-valued entropy bound then gives a half logarithm of the signal energy. No second moment of $`N`$ is needed.

An independent thinning argument controls the inaccessible-loss ceiling. The proof rewrites the counting coherent information using two binomially thinned counts, bounds thinning's entropy loss using its transition-matrix row sums, and bounds binomial entropy uniformly. Combining the energy and loss upper bounds produces a half logarithm of $`\min\{E,1/b\}`$.

The lower bound needs its own construction. A thermal average input makes the count conditioned on $`K=k`$ negative binomial. Its collision integral and a geometric lower-tail estimate supply the same leading order, using input mean $`\min\{E,1/b\}`$. See [Counting bounds](../science/counting_bounds.md) for each finite inequality. This matching argument does not prove thermal optimality at every finite parameter pair.

<a id="coherence"></a>
## Measuring number superpositions before producing a record

A two-level example distinguishes quantum preprocessing from classical forgetting. With $`b=0`$ on input support $`\{|0\rangle,|1\rangle\}`$, the number-measurement branch operators are

```math
A_0=|0\rangle\langle0|+\sqrt a|1\rangle\langle1|,
\qquad A_1=\sqrt c|0\rangle\langle1|.
```

Measuring the helper in the plus/minus basis instead gives $`A_\pm=(A_0\pm A_1)/\sqrt2`$. Each conditional map contains cross terms between $`A_0`$ and $`A_1`$ that classical processing of number outcomes cannot create. Both measurements are complete. This explains the mechanism, not a capacity advantage for the qubit-restricted model.

To see the purity calculation, first occupy photon numbers $`0,\ldots,d-1`$ and use all fourth-root phase vectors:

```math
|v_{\boldsymbol\omega}\rangle=\sum_{k=0}^{d-1}\omega_k|k\rangle,
\qquad
E_{\boldsymbol\omega}=4^{-d}|v_{\boldsymbol\omega}\rangle
\langle v_{\boldsymbol\omega}|,
\qquad \omega_k\in\{1,i,-1,-i\}.
```

The off-diagonal terms cancel when effects are summed. Adding the projector outside the occupied support completes the full-space POVM. The indexed operator $`E_{\boldsymbol\omega}`$ is a POVM effect; the unindexed scalar $`E`$ remains the signal-energy budget.

For a diagonal helper marginal the outcomes have equal probability. Expanding the conditional receiver purity and averaging phases leaves two pairings, with their shared diagonal contribution subtracted. This gives

```math
\mathbb E_{\boldsymbol\omega}\mathrm{Tr}\,\rho_{B|\boldsymbol\omega}^{2}
\le\mathrm{Tr}\,\rho_B^2+\mathrm{Tr}\,\rho_{BD}^2.
```

Fourth-root phases eliminate extra pairings that independent signs would retain. The argument is written fully in [Coherent measurements](../science/coherent_measurements.md); it is not an appeal to an unproved random-state approximation.

Entropy versus purity, Jensen's inequality, and the thermal identities now yield the achievable lower bound

```math
Q_1(E)\ge\max\{0,R_1(E)\},
```

```math
R_1(E)=-\log_2\!\left[
\frac1{1+2aE}+\frac1{1+2(1-b)E}\right]-g(bE).
```

A separate finite detector is used on each collected mode. The independent-phase family explains the moment calculation. For an odd prime $`q\ge d`$, the established phases $`\omega_k(r,s)=e^{2\pi i(rk+sk^2)/q}`$ reproduce the same pairings. Each fixed $`s`$ already defines a complete Fourier POVM; selecting a setting with small average receiver purity retains the rate bound with $`q<2d`$ occupied outcomes. The choice depends on the specified channel and average input, never on the unknown message. See [Coherent measurements](../science/coherent_measurements.md) for the exact construction and its attribution.

<a id="limits"></a>
## Keep the three limits separate

First fix a photon cutoff and a finite detector. Then use sufficiently long endpoint codes at that fixed channel to approach an achievable rate. Only afterward increase the cutoff. Truncating a thermal input gives strict signal-energy slack, and its explicit geometric tail controls the output entropy correction. Trace-norm convergence alone would not justify entropy convergence on an unbounded oscillator.

The large-energy/near-complete-collection comparison is another limit. Fix $`0\lt a\lt 1`$, take $`E\ge1`$ and $`0\le b\le\frac12\min\{a,1-a\}`$, and put $`L=\min\{E,1/b\}`$ with $`1/0=\infty`$. Only along paths with $`L\to\infty`$ does the ratio of the two leading laws tend to two. At fixed $`b>0`$, increasing $`E`$ eventually reaches a loss-limited scale; that is not the same ratio limit. With no collected output, all detector classes coincide with ordinary pure loss, outside the stated half-logarithmic domain.

<a id="record-resources"></a>
## Finite cutoff, transmitted record, and detector accuracy

For a thermal input of mean $`x`$ restricted to $`d`$ levels, the omitted mass is $`t=[x/(1+x)]^d`$. The positive mixture of the retained state and the tail gives a one-sided rate penalty at most $`-2\log_2(1-t)`$. Fixed tail tolerance therefore needs $`O(x+1)`$ levels. This estimate supplies an explicit construction while leaving the converse's mean-energy input class unrestricted.

The selected detector has $`q<2d`$ occupied outcomes, plus an outside flag. A finite record must include every announced setting and retained outcome. The [record account](../science/detector_resources.md) matches the leading $`\log_2L+O(1)`$ record cost for a bounded rate gap and gives the separate record-capacity tradeoff. An alphabet size is not a physical gate count.

When a detector is imperfect, compare its actual receiver state with a purification of the chosen input retained:

```math
I_c(\rho,\Phi)=-S(R|BX).
```

A finite dimension for $`R`$ permits a conditional-entropy continuity bound. The formula includes any unresolved apparatus through the actual channel; replacing its full complement by the original optical output $`Z`$ could give the wrong rate. The coding statement uses the implemented memoryless channel, rather than promising that an ideal decoder works unchanged.

<a id="phase-reference"></a>
## Supply a finite phase reference and retain its discarded information

A coherent detector mixes number levels. The [finite-reference construction](../science/finite_reference.md) implements a prescribed $`q`$-level unitary with a sine-shaped reference state on $`K_{\rm ref}`$ consecutive photon levels, starting at $`h=q-1`$. Its initial mean photons are $`h+(K_{\rm ref}-1)/2`$. Within each occupied total-number sector, the joint unitary acts as

```math
|k\rangle_D|n\rangle_W\longmapsto
\sum_{j=0}^{q-1}U_{jk}|j\rangle_D|n+k-j\rangle_W.
```

The reference supplies or absorbs the change in detector photon number. Boundary margins keep every shift on a nonnegative ladder. The construction is number conserving, but the reference can change and become correlated. Fresh independent references give a memoryless detector. Initial stock, net energy transfer, and the cost of preparing or resetting that stock are different quantities.

Approximating the full prescribed gate uniformly is one resource question. For communication, the [direct argument](../science/direct_reference.md) instead bounds the information left in the discarded reference. The actual complementary output includes $`ZW`$ and a copy of the count $`Y`$, so

```math
I_c=S(B|Y)-S(ZW|Y).
```

Each conditional reference is a mixture of translated sine states in an interval of length $`K_{\rm ref}+d-1`$. A discrete-Laplacian energy estimate and the maximum-entropy principle give

```math
S(W|Y)\le g\!\left[\frac{\pi^2}{12}(2r+r^2)\right],
\qquad r=\frac{d-1}{K_{\rm ref}+1}.
```

The Laplacian mode number is an auxiliary mathematical observable, not the reference's physical photon energy. Choosing $`K_{\rm ref}`$ proportional to $`d`$ makes this entropy penalty a constant. Meanwhile, the actual conditional receiver is a mixture of number rotations of the ideal conditional state, so its entropy cannot decrease. Subadditivity pays the complete $`ZW`$ complement and retains the ideal rate up to that constant. With $`d=O(L+1)`$, fresh initial reference photons $`O(L+1)`$ suffice.

<a id="local-reference"></a>
## A converse for reference stock, and the resulting capacity profile

To ask whether that stock is necessary, specify the allowed operations. The local-reference model starts the apparatus independently of the encoded signal and requires every effective helper effect $`E_y`$ to satisfy

```math
[E_y,N_{D_i}+N_{W_i}]=0\quad\text{for every mode }i.
```

Preserving only the sum across all modes is a weaker restriction and permits additional operations. Under separate local invariance, revealing each conserved total can only help the receiver. The all-code converse then bounds logical coherent information by conditional number entropies $`H(J_i|T_i)`$, with $`T_i=N_{D_i}+N_{W_i}`$. It does not twirl an arbitrary competing input or assume that the implemented detector is degradable.

The [width proof](../science/reference_width_bounds.md) uses a residual second moment to bound reference variance and support width. Mean stock requires a different estimate: large variance is possible at mean one. The [mean-energy proof](../science/reference_mean_bounds.md) uses the first absolute residual moment and unit-interval dithering, followed by the Laplace maximum-entropy bound. With average initial reference mean $`M`$, it gives

```math
Q_{\rm loc}^{\rm mean}(E,M)\le
\min\!\left\{Q_{\rm coll}(E),
\log_2\!\left[2e\left(
\sqrt{\frac{a(a+c)}cE}+\frac acM+\frac14\right)\right]\right\}.
```

The estimate permits infinite reference variance. Combining it with counting and the direct sine-reference construction yields

```math
Q_{\rm loc}^{\rm mean}(E,M)
=\min\!\left\{\log_2E,
\max\!\left\{\tfrac12\log_2E,\log_2(M+1)\right\}\right\}+O_a(1).
```

This profile has unrestricted classical records and holds for fixed $`0\lt a\lt 1`$, $`E\ge1`$, $`M\ge0`$, $`0\le b\le\frac12\min\{a,1-a\}`$, and $`bE\le1`$. If $`M+1`$ scales as $`E^\alpha`$, the leading coefficient is:

| Reference exponent | Rate coefficient multiplying $`\log_2E`$ |
|---|---:|
| $`0\le\alpha\le1/2`$ | $`1/2`$ |
| $`1/2<\alpha<1`$ | $`\alpha`$ |
| $`\alpha\ge1`$ | $`1`$ |

Linear mean stock suffices for a bounded additive rate gap, and such a gap requires $`M=\Omega(E)`$ within this model. Leading coefficient one is weaker: $`M=E/\log E`$ still leaves a growing logarithmic-of-logarithmic gap. The mean profile and the separate classical-record profile do not jointly optimize both resource budgets.

<a id="synthesis"></a>
## Assemble the result and its boundaries

The counting converse and construction give $`Q_{\rm cnt}=\frac12\log_2L+O_a(1)`$. The coherent lower bound and inherited collective upper bound give $`Q_1=\log_2L+O_a(1)`$. Their finite-energy comparison also proves

```math
0\le Q_{\rm coll}(E)-Q_1(E)\le\log_2e.
```

Thus photon-number coherence within an individual collected mode is enough for the full leading rate, while unrestricted processing of count records is not. All comparisons retain arbitrary endpoint quantum coding. Photon counting is itself non-Gaussian, so this is not a Gaussian-versus-non-Gaussian theorem.

The [finite certificates](../verification/README.md) evaluate proved inequalities. The unrestricted optical example uses a mean budget; the [two-photon example](../science/qubit_optical_bridge.md) imposes an additional per-mode cutoff. Neither is an experimental implementation or a numerical substitute for an all-input proof.

The finite-reference analysis strengthens the physical account: prepared reference photons can be charged, and their mean determines the local-conservation capacity profile to an additive constant. The [interpretation](../science/interpretation.md) and [attribution](../references/RELATED_WORK.md) keep the underlying operation contracts, inherited ingredients, and unoptimized synthesis, preparation, and reset costs explicit.
