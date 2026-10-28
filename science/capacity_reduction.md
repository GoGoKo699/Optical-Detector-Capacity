# From arbitrary codes to entropy bounds

[Model](model.md) · [Counting](counting_bounds.md) · [Coherent detector](coherent_measurements.md)

The collective capacity and the output-degradation method are inherited from the [partial-monitoring result](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/447726d37438de67b4ef2e1a9406d2c44d6a394f/research/PROOF_DEPENDENCIES.md). This page reconstructs the needed argument with the present notation. Assistance and energy-constrained channel coding have the primary attributions in [Related work](../references/RELATED_WORK.md).

## Joint degradation, not just a marginal relation

Let $`\mathcal L_t`$ be vacuum attenuation with retention $`t`$. For $`a\ge b`$ and $`a>0`$,

```math
\mathcal N_{ZD}=(\mathcal L_{b/a}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

This is a channel identity, including correlations with any reference. In the Weyl convention $`W(z)=\exp(z\hat a^\dagger-z^*\hat a)`$,

```math
\mathcal N_{BD}^*[W(z)\otimes W(w)]
=e^{-\{ |z|^2+|w|^2-|\sqrt a z+\sqrt c w|^2\}/2}
 W(\sqrt a z+\sqrt c w),
```

while $`\mathcal L_t^*[W(z)]=e^{-(1-t)|z|^2/2}W(\sqrt t z)`$. Composition replaces $`a`$ by $`b`$ in the first formula. Equality on Weyl operators determines the normal channels on the full Fock space. The helper register is unchanged.

For a rank-one helper measurement with rows $`m_x`$, put $`W_x=(I_{BZ}\otimes m_x)V`$. The measured channel has receiver output $`BX`$ and complement $`ZY`$, where $`Y`$ is a copy of the classical outcome. It is degradable by $`\mathcal L_{b/a}`$ and flag copying, and

```math
I_c(\rho,\mathcal N_M)=S(B|X)-S(Z|X).
```

The inaccessible quantum system alone is not the complement: the flag must be retained. For coarse measurements there can also be an unresolved helper system. This distinction matters when a record is discarded.

## Collective converse with arbitrary encoders

Purify an encoded block as $`RFA^n`$, where $`R`$ is the finite logical reference and $`F`$ is a discarded encoder system. For a finite helper POVM with effects $`Q_x`$, represent outcome $`x`$ by the mathematical filter $`\sqrt{Q_x}:D^n\to G`$. Conditional on an outcome, $`RFB^nZ^nG`$ is pure. Tracing $`G`$ gives exactly the actual receiver/reference state.

Joint degradation commutes with this filter. Applying it to $`B^n`$ produces a second $`Z'^n`$ with the same $`FGZ^n`$ marginal. Weak monotonicity therefore gives $`S(FG|Z^n,x)\ge0`$. It follows that

```math
\begin{aligned}
I(R\rangle B^nX)
&=S(B^n|X)-S(FGZ^n|X)\\
&\le S(B^n|X)-S(Z^n|X)\\
&\le S(B^n)-S(Z^n).
\end{aligned}
```

The last step is $`I(X;Z^n)\le I(X;B^n)`$ under the same degrading channel. Decoding cannot increase coherent information. No isometric-encoder restriction or fine-measurement assumption is imposed on a competing protocol.

All averaged conditional entropies used here are finite: conditional purity gives $`S(FGZ^n|X)=S(RB^n|X)\le\log_2d_n+ng(aE)`$, and $`S(Z^n|X)\le ng(bE)`$. Subadditivity bounds $`S(FG|X)`$ by their sum. A physical energy bound on the proof register $`G`$ is unnecessary.

For a normal record on a standard Borel space, apply the finite-record argument to increasing finite partitions. The receiver/reference conditional state fields converge in integrated trace norm. Conditional-entropy continuity on the finite system $`R`$ passes the bound to the complete record. Equivalently, mutual information $`I(R;B^nX)`$ is the increasing limit over these partitions. No differential entropy is introduced.

## Thermal reference supplies the all-input energy bound

Let the actual mean input occupation per use be $`\bar E\le E`$. For $`b>0`$ and $`\bar E>0`$, the thermal logarithm gives

```math
D(\rho_{B^n}\Vert\tau_{a\bar E}^{\otimes n})
=ng(a\bar E)-S(B^n),
```

and the analogous formula for $`Z^n`$. Product attenuation maps the first thermal reference to the second. Relative-entropy contraction yields

```math
S(B^n)-S(Z^n)\le n[g(a\bar E)-g(b\bar E)]
\le n[g(aE)-g(bE)].
```

The final function is increasing when $`a>b`$: $`t\ln(1+1/(tE))`$ increases with $`t`$. The cases $`b=0`$ and $`\bar E=0`$ use the direct vacuum and maximum-entropy bounds. This covers correlated, non-Gaussian, and heavy-tailed competing inputs.

High entanglement fidelity forces the decoded coherent information to approach $`\log_2d_n`$ per block, with the finite-reference continuity correction. Dividing by $`n`$ gives the capacity upper bound without assuming a bound on $`d_n`$ beforehand.

## Attaining the collective benchmark

Fix a finite photon cutoff for a truncated thermal average input, then a sufficiently large helper block. The established pure-state assistance theorem, applied mathematically to $`B:(RZ):D`$, supplies a helper measurement with average $`B`$ entropy approaching the smaller of $`S(B)`$ and $`S(BD)`$ per use. This involves no operation on the inaccessible group $`RZ`$. Concavity bounds the average conditional $`Z`$ entropy by $`S(Z)`$.

Freeze that finite measurement into a flagged channel. Ordinary energy-constrained quantum coding attains its coherent information with the flag sent only to the receiver. Coding is performed at fixed cutoff and fixed helper block; only then are they increased. The truncated thermal mean is strictly below $`E`$, supplying energy slack.

To justify the entropy limit, for $`r=E/(1+E)`$ the omitted tail beyond $`M`$ has probability $`\delta_M=r^{M+1}`$ and conditional mean $`M+1+E`$. After attenuation with retention $`s`$, its entropy is at most $`g(s(M+1+E))`$. The entropy-of-mixture bound makes the correction at most a binary entropy and terms of order $`\delta_M g(s(M+1+E))`$, which vanish. In the limit $`S(B)=g(aE)\le g((1-b)E)=S(BD)`$. This proves

```math
Q_{\rm coll}(E)=g(aE)-g(bE)\quad(a>b).
```

When $`a\le b`$, the reversed joint degradation constructs a second receiver with the same reference marginal even after the helper measurement. The no-cloning/antidegradability bound rules out positive quantum rate. The case $`a=0`$ is directly measure-and-prepare.

## Exact counting reduction

For exact number measurement, the flagged channel and its complement have output entropies at most $`g(aE)+g(cE)`$ and $`g(bE)+g(cE)`$. The number observable satisfies the Gibbs condition. The energy-constrained degradable-channel theorem therefore applies directly. Phase covariance and concavity of coherent information permit averaging the input over $`e^{-i\theta\hat n}`$, without increasing its energy.

Consequently, for $`a>b`$,

```math
Q_{\rm cnt}(E)=
\sup_{p:\,\sum_n np_n\le E}
\{H(J|K)-H(W|K)\}.
```

Both entropies are evaluated under the multinomial law in the model. The supremum permits every photon-number distribution of finite mean. The input is the average of a quantum code, not a restriction to transmitting classical number states.

Degradable-channel additivity excludes an advantage from correlated endpoint code inputs beyond this optimization; equivalently, the difference between summed one-use coherent informations and the block coherent information is the contraction of output total correlation to complementary total correlation. Concavity in the energy allowance accounts for arbitrary allocation across modes. Classical postprocessing of the full count vector cannot improve the quantum channel.
