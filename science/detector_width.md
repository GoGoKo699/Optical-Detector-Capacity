# Number-conserving detector width

[Model](model.md) · [Counting bounds](counting_bounds.md) · [Coherent detector](coherent_measurements.md) · [Related work](../references/RELATED_WORK.md)

Suppose the helper measures disjoint, predetermined blocks of at most $`m`$ collected modes. Every effect of a block measurement commutes with each spectral projector of the total photon number of that block. It measures each block independently with settings fixed in advance, and sends a classical record to the receiver. The sender and receiver can use arbitrary endpoint codes. Within a total-number sector the helper can use general coherent control.

Fix $`0<a<1`$, $`E\ge1`$, and $`0\le b\le \min\{a,1-a\}/2`$, and write $`c=1-a-b`$, $`L=\min\{E,1/b\}`$, and $`1/0=\infty`$. The quantum capacity per original mode satisfies

```math
Q_{\le m}(E,b)=\left(1-\frac{1}{2m}\right)\log_2 L+O_a(1).
```

The additive bound is uniform in $`E,b,m`$. The proof separates the residual uncertainty in the total received count from the additional information carried within each fixed-number sector. At width one the latter disappears and the ordinary counting law is recovered. Width two gives the coefficient $`3/4`$.

## Reduction to entropy differences

For a block of $`r`$ modes, first consider a finite partition of any normal detector record. Decompose each resulting effect within each collected total-number sector into rank-one effects, using the columns of its positive square root in an occupation basis. This refines the record to a flag $`Y`$ that includes the exact helper total $`K`$. The flag has finite entropy: the coarse alphabet is finite, $`K`$ has finite mean, and at most $`d_r(k)=\binom{k+r-1}{r-1}`$ fine effects per coarse outcome occur at $`K=k`$.

The refined channel has output $`BY`$ and complement $`ZY'`$, with a copy $`Y'`$ of the flag. The inherited [joint degradation](capacity_reduction.md#joint-degradation-not-just-a-marginal-relation) attenuates $`B`$ to $`Z`$ with retention $`b/a`$ even conditional on a helper flag. Thus the refined channel is degradable, and its coherent information is $`S(B|Y)-S(Z|Y)`$. The same reasoning applies to a product of predetermined block detectors. For an arbitrary encoder with discarded environment $`F`$, weak monotonicity with the original and simulated complements gives $`S(F|Z^nY')\ge0`$. The logical-reference coherent information at the receiver is then at most the coherent information of the actual average input through the refined channel. The latter is bounded by the sum of the block coherent informations, by contraction of total correlation under the product degrading channel. The receiver can recover the original coarse record from the fine one. Finite partitions tend to the full normal record as in the [arbitrary-code converse](capacity_reduction.md#collective-converse-with-arbitrary-encoders), using conditional-entropy continuity on the finite logical reference.

For each block the coherent information is concave in its average input. Global phase rotation on the input block changes the conditional outputs by the corresponding rotations on $`B`$ and $`Z`$, because the effects commute with the helper's total number. Twirling the input by this phase can only increase coherent information and leaves mean energy unchanged. In the resulting state, the $`B`$ and $`Z`$ outputs are block diagonal in their respective totals $`J`$ and $`W`$ conditional on $`Y`$.

## Converse: one count and its number sectors

Conditional on the total input occupation $`N`$, the triple $`(J,W,K)`$ has the ordinary multinomial law with fractions $`(a,b,c)`$. This holds for every input state within a fixed $`N`$ sector. Indeed, the product splitter intertwines a common passive $`U(r)`$ on the input and on its three outputs. The probability effect for any fixed output totals commutes with the irreducible representation on $`\operatorname{Sym}^N(\mathbb C^r)`$, so is scalar. Its value comes from sending all $`N`$ photons through one mode.

Write the block coherent information as
```math
H(J|Y)-H(W|Y)
+\sum_{y,j}p(y,j)S(B_{j|y})-\sum_{y,w}p(y,w)S(Z_{w|y}).
```
The degrading channel reproduces the joint law of the inaccessible count and flag by thinning $`J`$, to the inaccessible count with retention $`b/a`$, conditional on any flag. Therefore $`I(J;Y|K)\ge I(W;Y|K)`$. The first entropy difference is at most $`H(J|K)-H(W|K)`$. The [scalar counting bounds](counting_bounds.md) apply to this aggregate multinomial law. If the input mean per mode in the block is $`e`$, they give the two upper bounds $`\tfrac12\log_2(1+re)+O_a(1)`$ and, for $`b>0`$, $`\tfrac12\log_2(1/b)+O_a(1)`$.

For the energy bound on the sector contribution, drop the nonnegative output sector entropies and use $`S(B_{j|y})\le \log_2 d_r(j)`$. For $`r\ge2`$ the binomial estimate gives
```math
\log_2 d_r(j)\le (r-1)\log_2\!\left[\mathrm e\left(1+\frac{j}{r-1}\right)\right].
```
By concavity and $`\mathbb E J=are`$, the result is at most $`(r-1)\log_2(1+e)+O_a(r)`$. At $`r=1`$ the sector entropy vanishes.

For the loss bound, at fixed $`J=j`$ the conditional attenuation into $`W=w`$ is a normalized covariant channel from the sector of dimension $`d_r(j)`$ to the sector of dimension $`d_r(w)`$. The event probability is the scalar binomial thinning probability, by the same intertwining argument used for the splitter. Covariance maps the maximally mixed state of the first sector to that of the second. Relative entropy contraction bounds the difference of their state entropies by $`\log_2[d_r(j)/d_r(w)]`$. The actual $`Z_{w|y}`$ mixes these outputs over $`j`$, so concavity bounds the sector contribution by $`\mathbb E\log_2[d_r(J)/d_r(W)]`$. Since $`W\le J`$,
```math
\begin{aligned}
\frac{d_r(j)}{d_r(w)}
&=\prod_{\ell=1}^{r-1}\frac{j+\ell}{w+\ell}
\le\left(\frac{j+1}{w+1}\right)^{r-1},\\
\mathbb E\!\left[\left.\frac{J+1}{W+1}\right|J=j\right]
&=\frac{1-(1-b/a)^{j+1}}{b/a}\le \frac{a}{b}.
\end{aligned}
```
The second identity follows by replacing $`\binom jw/(w+1)`$ by $`\binom{j+1}{w+1}/(j+1)`$. Jensen's inequality bounds the sector contribution by $`(r-1)\log_2(a/b)`$.

Since $`1+re\le r(1+e)`$, the two complete block upper bounds are $`(r-\tfrac12)\log_2(1+e)+O_a(r)`$ and $`(r-\tfrac12)\log_2(1/b)+O_a(r)`$. For a partition with block sizes $`r_i\le m`$, one has $`r_i-\tfrac12\le r_i(1-\tfrac1{2m})`$. In the energy bound, weighted Jensen uses $`\sum_i r_i e_i\le nE`$ with $`n=\sum_i r_i`$. Dividing by $`n`$ and taking the smaller bound gives the claimed converse, since $`\log_2(1+E)\le\log_2 E+1`$. At $`b=0`$ the energy bound suffices.

## Construction: a Fourier measurement within each sector

Use $`m`$ independent thermal average inputs of mean $`L`$. Given collected total $`K=k`$, the received total $`J`$ is the sum of $`s=k+m`$ geometric variables of mean $`\mu=aL/(1+cL)`$. To see this, represent each input occupation as Poisson with an exponential intensity of mean $`L`$. The total intensity across the block is gamma with shape $`m`$ and rate $`1/L`$. Conditioning on the helper's Poisson count changes these to shape $`k+m`$ and rate $`1/L+c`$. The conditional law of the received Poisson count after mixing over this gamma distribution is negative binomial. Write its point probabilities as $`p_j`$.

Conditional on $`J=j,K=k`$, both individual sector marginals are maximally mixed by common $`U(m)`$ covariance. The corresponding $`BD`$ state is uniform on a subspace of rank $`d_m(j+k)`$. Indeed, after tracing $`Z`$ one can first attenuate to the retained thermal modes with fraction $`a+c`$, then split those into $`B,D`$. On the total $`j+k`$ sector, the component of this splitter with totals $`j,k`$ is proportional to an isometry by covariance and irreducibility. Conditional on $`k`$, the $`BD`$ state is a direct sum over $`j`$, since the thermal input was already total-number diagonal. Consequently
```math
\operatorname{Tr}\rho_{BD|k}^2
=\sum_j\frac{p_j^2}{d_m(j+k)}
\le\sum_j\frac{p_j^2}{d_m(j)}
=\operatorname{Tr}\rho_{B|k}^2.
```

The helper marginal at $`k`$ is maximally mixed on a sector of dimension $`d=d_m(k)`$. For a vector of fourth-root phases $`(\eta_\ell)_{\ell=0}^{d-1}`$, measure in the orthonormal basis with components $`d^{-1/2}\eta_\ell\exp(2\pi i u\ell/d)`$, for $`u=0,\ldots,d-1`$. Its outcomes at this thermal input are uniform. Write $`C_{\ell t}`$ for the helper occupation-basis blocks of $`\rho_{BD|k}`$. Averaging the conditional receiver purity over independent uniform fourth-root phases leaves two paired terms in the phase expansion and subtracts the common diagonal term. For each $`u`$, the result is
```math
\operatorname{Tr}\rho_{B|k}^2+\operatorname{Tr}\rho_{BD|k}^2
-\sum_\ell \operatorname{Tr} C_{\ell\ell}^2
\le 2\operatorname{Tr}\rho_{B|k}^2.
```
The fixed Fourier factors cancel on every surviving pairing. This is the [same phase moment](coherent_measurements.md#exact-phase-averaged-purity) used for the coherent single-mode detector. Choose one deterministic mask in each $`k`$ sector whose mean purity over basis outcomes is at most the phase average. The measurement is now fixed and reports $`(k,u)`$. This direct sum of sector basis changes preserves total number. On finite occupied support it can be implemented by a number-preserving basis change followed by occupation counting.

## Uniform rate and finite cutoff

The geometric mean parameter obeys $`a/(2-a)\le\mu\le 2a/(1-a)`$ because $`L\ge1`$ and $`c\ge (1-a)/2`$. The negative-binomial point probabilities satisfy $`\max_j p_j\le C_a/\sqrt{s}`$. Fourier inversion gives this bound: the modulus of the geometric characteristic function is $`[1+4\mu(1+\mu)\sin^2(t/2)]^{-1/2}`$, which is bounded by $`\exp(-c_a t^2)`$ for $`|t|\le\pi`$ with $`c_a>0`$. The $`s`$-fold product integrates to $`O_a(s^{-1/2})`$.

Let $`\alpha=\tfrac12\ln(1+\frac{a}{2-a}(1-\exp(-1)))>0`$. If $`j<\alpha s`$, Markov's inequality applied to $`\exp(-J)`$ gives $`p_j\le\exp(-\alpha s)`$. For $`j\ge\alpha s`$ use $`d_m(j)\ge(\alpha s/m)^{m-1}`$, including $`m=1`$ with sector dimension one. The small-$`j`$ bound also has the desired decay: for $`x=s/m\ge1`$,
```math
\exp(-\alpha s)\sqrt{s}(s/m)^{m-1}
\le \sqrt m\, [x\exp(-\alpha x)]^m\le C_a^m.
```
Thus $`\operatorname{Tr}\rho_{B|k}^2\le\max_j[p_j/d_m(j)]\le C_a^m s^{-1/2}(s/m)^{-(m-1)}`$. Von Neumann entropy dominates collision entropy. Jensen applied to the average purity after the chosen basis gives
```math
\mathbb E_u S(B_{k,u})\ge
(m-\tfrac12)\log_2[(k+m)/m]-O_a(m).
```
The helper count is the sum of $`m`$ independent geometric counts $`K_i`$ of mean $`cL`$. By the arithmetic–geometric mean inequality and the [geometric logarithmic estimate](counting_bounds.md#thermal-average-input-supplies-the-lower-bound),
```math
\mathbb E\log_2[(K+m)/m]
\ge \mathbb E\log_2(1+K_1)
\ge \log_2(1+cL)-\log_2\mathrm e.
```
Finally $`S(Z|Y)\le S(Z)=m g(bL)\le m g(1)`$, where $`g`$ is the thermal entropy. The block coherent information is at least $`(m-\tfrac12)\log_2L-O_a(m)`$.

For coding, fix $`E,b,m`$ and the thermal-input choices of sector bases. Project the average input to a finite total cutoff $`N\le M`$ and normalize, leaving strict energy slack. In the original thermal state, let $`\delta`$ be the excluded probability. Adding the binary cutoff label to the record changes each conditional entropy by at most $`h_2(\delta)`$. The weighted tail entropies of $`B`$ and $`Z`$ are at most $`\delta m g(aL/\delta)`$ and $`\delta m g(bL/\delta)`$, both vanishing with $`\delta`$. Thus the cutoff input approaches the claimed coherent information under the same sector measurements. Only $`k,j,w\le M`$ occur on coded inputs. A single overflow effect completes the finite measurement, with zero probability on that input subspace. Finite-dimensional coherent-information coding with the energy slack applies to repeated independent $`m`$-mode channels. The capacity limit is taken for the fixed block before comparing different widths.

## What a passive mixer supplies

A single predetermined passive $`U(r)`$ on the collected modes followed by ordinary occupation counting has the same optimized capacity as counting. The identical splitters intertwine an input $`U(r)`$ with $`U(r)`$ on all three outputs. An input rotation and an inverse receiver rotation reproduce the detector's complete classical–quantum output, up to the receiver's removable unitary. Both rotations preserve the model's resource constraints. This equivalence concerns the fixed mixer on the detected modes followed by counting. The sector Fourier construction permits general number-preserving control within those modes.

The [collective benchmark](capacity_reduction.md#attaining-the-collective-benchmark) is $`\log_2L+O_a(1)`$. The gap to the width-limited capacity is therefore $`\log_2 L/(2m)+O_a(1)`$. Width of order $`\log L`$ suffices for a bounded gap, and a fixed bound on the gap requires at least that order of width. The width law measures detector block size. The basis changes and physical implementation costs depend on the occupied sectors.
