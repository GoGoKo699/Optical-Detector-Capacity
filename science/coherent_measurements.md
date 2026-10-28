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

This is one fixed finite POVM, not postselection or a choice conditioned on the unknown message. It can be repeated separately on every collected mode. Its $`4^d`$ outcomes and general coherent control are not asserted efficient. A phase reference permits the superpositions between different photon numbers.

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

## Removing the cutoff with the signal budget intact

A thermal input of mean $`E`$ gives a thermal receiver of mean $`aE`$. The joint $`BD`$ output is unitarily equivalent to a thermal mode of mean $`(1-b)E`$ and a vacuum mode. Hence

```math
\mathrm{Tr}\,\rho_B^2=\frac1{1+2aE},\qquad
\mathrm{Tr}\,\rho_{BD}^2=\frac1{1+2(1-b)E},\qquad
S(\rho_Z)=g(bE).
```

Truncated thermal inputs have mean strictly smaller than $`E`$. Their outputs converge in trace norm, so the purities converge. The explicit geometric-tail entropy bound in the [operational reduction](capacity_reduction.md) gives convergence of $`S(\rho_Z)`$ as well; entropy convergence is not inferred from trace norm alone.

At every fixed cutoff, apply the energy-constrained coding theorem to the finite-input flagged channel. Its finite output alphabet and photon support ensure finite output entropy, and the input has energy slack. Only after this coding limit is taken does the cutoff increase. Thus, for $`E>0`$ and $`a>b`$,

```math
Q_1(E)\ge\max\{0,R_1(E)\},
```

```math
R_1(E)=-\log_2\!\left[
\frac1{1+2aE}+\frac1{1+2(1-b)E}\right]-g(bE).
```

At zero energy the capacity is zero. The displayed bound is a supremum-limit statement: any strictly smaller positive rate is attained by some finite cutoff and finite detector followed by sufficiently long codes. It does not specify a practical cutoff or gate count.

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
