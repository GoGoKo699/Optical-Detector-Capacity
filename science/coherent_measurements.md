# A finite coherent detector on each collected mode

[Model](model.md) · [Operational reduction](capacity_reduction.md) · [Uniform laws](uniform_laws.md)

Counting distinguishes the helper's number states. Here a POVM uses superpositions of them before producing a record. Random-phase and Fourier assistance are established techniques; the finite purity calculation below supplies the particular rate bound needed for the optical detector comparison.

## A complete finite POVM

First restrict the average input to photon numbers $`0,\ldots,M`$. All splitter outputs then have that support. Set $`d=M+1`$. For each vector $`\boldsymbol\omega\in\{1,i,-1,-i\}^{d}`$, define

```math
|v_{\boldsymbol\omega}\rangle=\sum_{k=0}^{M}\omega_k|k\rangle,
\qquad
E_{\boldsymbol\omega}=4^{-d}|v_{\boldsymbol\omega}\rangle
\langle v_{\boldsymbol\omega}|.
```

Averaging the independent phases cancels every off-diagonal term, so the effects sum to the identity on this subspace. Add the projector onto its orthogonal complement to obtain a POVM on the full Fock space. That last outcome has zero probability for the chosen cutoff code, not for arbitrary competing inputs.

This is one fixed finite POVM, not postselection or a choice conditioned on the unknown message. It can be repeated separately on every collected mode. A phase reference permits the superpositions between different photon numbers. The exponential family makes the moment calculation transparent; the construction below reduces its outcome count without changing the rate bound.

## Exact phase-averaged purity

Use a truncated thermal average input. Its helper marginal is diagonal. Write

```math
\rho_{BD}=\sum_{k,l}C_{kl}\otimes|k\rangle\langle l|.
```

Every phase outcome has probability $`4^{-d}`$. Its normalized receiver state is

```math
\sigma_B(\boldsymbol\omega)=\sum_{k,l}\omega_k^*\omega_l C_{kl}.
```

In a fourth-root-phase average, a product of two phase differences survives exactly when its indices pair. The diagonal pairing counted twice must be subtracted. Consequently

```math
\mathbb E_{\boldsymbol\omega}\mathrm{Tr}\,\sigma_B^2
=\mathrm{Tr}\,\rho_B^2+\mathrm{Tr}\,\rho_{BD}^2
-\sum_k\mathrm{Tr}\,C_{kk}^2
\le\mathrm{Tr}\,\rho_B^2+\mathrm{Tr}\,\rho_{BD}^2.
```

Independent signs alone would leave additional fourth moments; fourth roots remove them. The [finite checks](../verification/README.md) enumerate every outcome in small dimensions and verify the exact subtraction term as well as POVM completeness.

Von Neumann entropy dominates collision entropy, and $`-\log`$ is convex. Concavity bounds the corresponding average conditional loss entropy. Thus the flagged channel satisfies

```math
\begin{aligned}
I_c&=\mathbb E[S(\sigma_B)-S(\sigma_Z)]\\
&\ge-\log_2[\mathrm{Tr}\,\rho_B^2+\mathrm{Tr}\,\rho_{BD}^2]-S(\rho_Z).
\end{aligned}
```

The equality uses a complete rank-one measurement on the occupied helper support. It does not discard failures or an unresolved complementary register.

## Quadratic phases reproduce the same moments

The following phase ensemble is an established projective toric 2-design: Iosue, Mooney, Ehrenberg, and Gorshkov, [Theorem 2.7](https://arxiv.org/html/2311.13479v3#S2.SS1), tracing the construction to Iosue, Sharma, Gullans, and Albert, [Theorem C.9](https://arxiv.org/html/2211.05127v3). Its use here is to preserve the optical helper's purity bound with fewer outcomes. The design and the quadratic-phase primitive are inherited ingredients.

For $`d\ge2`$, choose the smallest odd prime $`q\ge d`$ and write $`\zeta=e^{2\pi i/q}`$. For $`r,s\in\{0,\ldots,q-1\}`$, put

```math
\omega_k(r,s)=\zeta^{rk+sk^2},\qquad
|v_{r,s}\rangle=\sum_{k=0}^{d-1}\omega_k(r,s)|k\rangle,
\qquad E_{r,s}=q^{-2}|v_{r,s}\rangle\langle v_{r,s}|.
```

Character orthogonality gives the second moment $`\mathbb E_{r,s}\omega_k^*\omega_l=\delta_{kl}`$, proving completeness on the occupied subspace. The fourth moment is nonzero exactly when

```math
k+m=l+n\pmod q,\qquad k^2+m^2=l^2+n^2\pmod q.
```

Because $`q`$ is odd, the two equations imply $`km=ln`$. The unordered pairs $`\{k,m\}`$ and $`\{l,n\}`$, with multiplicity, are therefore the roots of the same quadratic. All labels lie below $`q`$, so equality in the field is equality of the original labels. The moment equals one for those two pairings and zero otherwise. This is precisely the moment used above, including its diagonal subtraction. The entire purity identity is unchanged.

There are at most $`q^2<4d^2`$ indexed effects, plus an effect for the unoccupied complement. Duplicate effects may be merged; in particular the indexing need not count distinct phase vectors. The dimension-one case uses its trivial one-outcome measurement.

For perspective, any positively weighted phase ensemble reproducing *all* these moments needs at least $`d(d-1)+1`$ distinct points. In its weighted function space, $`1`$ and the $`d(d-1)`$ functions $`\omega_k^*\omega_l`$ for $`k\ne l`$ are orthonormal. Their number cannot exceed the support size. This is the toric-design bound of the cited sources. It constrains universal exact moment reproduction, rather than every detector that attains the capacity lower bound.

## One predetermined Fourier measurement suffices

For each fixed $`s`$, the effects

```math
F_{r|s}=q^{-1}|v_{r,s}\rangle\langle v_{r,s}|,
\qquad r=0,\ldots,q-1,
```

already sum to the identity on the occupied subspace. The quadratic design is their uniform mixture over $`s`$, with the setting retained in the record. For the same truncated thermal average input, each outcome of a fixed setting has probability $`1/q`$. Let

```math
P_s=\frac1q\sum_r\mathrm{Tr}\,\sigma_B(r,s)^2,
\qquad C=\mathrm{Tr}\,\rho_B^2+\mathrm{Tr}\,\rho_{BD}^2.
```

The exact design identity implies $`q^{-1}\sum_sP_s\le C`$. Choose a setting $`s_*`$ minimizing $`P_s`$; thus $`P_{s_*}\le C`$. Entropy ordering, Jensen's inequality, and concavity of the inaccessible marginal entropy give, for this one complete measurement,

```math
I_c(F_{\cdot|s_*},\rho_A)
\ge-\log_2P_{s_*}-S(\rho_Z)
\ge-\log_2C-S(\rho_Z).
```

Consequently a fixed measurement with $`q<2d`$ nonzero coded outcomes retains the same finite-cutoff rate guarantee. The setting is chosen from the known splitter and chosen average coded input, before transmission. It is independent of the unknown message. No outcome is accepted or rejected. The exact-moment lower bound above does not apply to this selected setting, which need not reproduce all moments.

There is a direct finite-dimensional realization. On the first $`q`$ Fock levels define

```math
D_s|k\rangle=\zeta^{-sk^2}|k\rangle,
\qquad (\mathcal F_q)_{r k}=q^{-1/2}\zeta^{-rk}.
```

Apply $`\mathcal F_qD_s`$ and count the output number. Its effects restricted to the input code support $`k<d`$ are exactly $`F_{r|s}`$. Extend the unitary by the identity outside the first $`q`$ levels and retain an outside outcome; its probability is zero for this cutoff code. This implements the required measurement on the coded states, even when $`d<q`$; equality with a particular extension of the POVM on all other states is not required. Alternatively, use prime cutoffs $`d=q`$ throughout. Unbounded prime cutoffs suffice for the thermal limit.

The quadratic phase is a Kerr-type number-squared phase; the relation between Kerr evolution and phase measurements is already explicit in Eq. (15) of the cited continuous-variable-design paper. A finite Fock-space Fourier transform still requires coherent control and a phase reference. The construction bounds the number of settings, occupied levels, and classical outcomes. The [resource account](detector_resources.md) adds sufficient accuracy bounds and the Fourier stage's specified mean excitation change; physical gate count, reference preparation, work, and reset cost remain unresolved. Detector energy remains outside the signal budget. A selected setting needs at most $`\lceil\log_2q\rceil`$ record bits on the coded support, or an alphabet of $`q+1`$ symbols including the outside outcome. The choice of $`s_*`$ can depend on the cutoff and channel; a single setting uniform in every energy and accuracy is not asserted.

## Removing the cutoff with the signal budget intact

A thermal input of mean $`E`$ gives a thermal receiver of mean $`aE`$. The joint $`BD`$ output is unitarily equivalent to a thermal mode of mean $`(1-b)E`$ and a vacuum mode. Hence

```math
\mathrm{Tr}\,\rho_B^2=\frac1{1+2aE},\qquad
\mathrm{Tr}\,\rho_{BD}^2=\frac1{1+2(1-b)E},\qquad
S(\rho_Z)=g(bE).
```

Truncated thermal inputs have mean strictly smaller than $`E`$. Their outputs converge in trace norm, so the purities converge. The explicit geometric-tail entropy bound in the [operational reduction](capacity_reduction.md) gives convergence of $`S(\rho_Z)`$ as well; entropy convergence is not inferred from trace norm alone.

At every fixed cutoff, select the quadratic setting as above and apply the energy-constrained coding theorem to the resulting finite-input flagged channel. Its finite output alphabet and photon support ensure finite output entropy, and the input has energy slack. Only after this coding limit is taken does the cutoff increase. Thus, for $`E>0`$ and $`a>b`$,

```math
Q_1(E)\ge\max\{0,R_1(E)\},
```

```math
R_1(E)=-\log_2\!\left[
\frac1{1+2aE}+\frac1{1+2(1-b)E}\right]-g(bE).
```

At zero energy the capacity is zero. The displayed bound is a supremum-limit statement: any strictly smaller positive rate is attained by some finite cutoff and finite detector followed by sufficiently long codes. The [resource account](detector_resources.md) supplies an explicit sufficient cutoff and control-error estimate. Physical gate count remains unresolved.

## At most a constant is left for collective helper processing

Since $`1-b\ge a`$, put $`x=aE`$ and bound the purity sum by $`2/(1+2x)`$. Subtracting the individual-mode lower bound from the exact collective benchmark gives

```math
Q_{\rm coll}(E)-Q_1(E)
\le g(x)-\log_2(1+2x)+1\le\log_2e.
```

To check the final constant, the function on the middle line starts at one, has derivative

```math
\frac1{\ln2}\left[\ln(1+1/x)-\frac2{1+2x}\right]>0
\quad(x>0),
```

and tends to $`\log_2e`$. The derivative inequality follows by integrating $`1/t`$ or from $`\ln((1+y)/(1-y))\ge2y`$. Clipping $`R_1`$ at zero only strengthens the result. The ordering of detector classes supplies the nonnegative lower bound. When $`a\le b`$, both capacities vanish.

This theorem gives a capacity guarantee within a constant, not an exact optimum over individual-mode POVMs. It also does not say that all measurements with photon-number coherence work equally well.
