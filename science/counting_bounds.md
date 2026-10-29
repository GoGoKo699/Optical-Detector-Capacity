# Counting: two converses and a matching construction

[Model](model.md) · [Operational reduction](capacity_reduction.md) · [Uniform laws](uniform_laws.md)

Assume $`a>b\ge0`$ and $`c=1-a-b`$. The exact counting optimization is over all distributions $`p_n`$ with $`\mathbb EN\le E`$. Write $`h_n(t)=H(\mathrm{Bin}(n,t))`$.

## Every number-diagonal record is simulated by counting

Let a helper block POVM be diagonal in the product occupation basis:

```math
G_y=\sum_{\mathbf k}p(y|\mathbf k)
|\mathbf k\rangle\langle\mathbf k|,
\qquad p(y|\mathbf k)\ge0,\quad\sum_y p(y|\mathbf k)=1.
```

For every joint state of receiver, helper, and reference, the unnormalized conditional receiver-reference state is the sum of the exact-count conditional states weighted by $`p(y|\mathbf k)`$. Thus full counting followed by this classical stochastic map simulates the entire receiver channel, including its reference correlations. This conclusion does not assume diagonal inputs or a particular encoder.

For standard-Borel outcome spaces, replace $`p(y|\mathbf k)`$ by a classical Markov kernel $`p(dy|\mathbf k)`$; the same operator-valued integral gives the simulation.

Every decoder for the coarser record can consequently be used after full counting. Arbitrarily correlated diagonal block effects obey the same comparison. So do measurements made once per collected mode, with each diagonal POVM chosen classically from earlier outcomes: their complete transcript is a stochastic function of the exact occupation vector. They cannot exceed $`Q_{\rm cnt}`$. This is a data-processing consequence of the detector definition, rather than an additional capacity formula. Coherent processing or remeasurement must be assessed through the resulting effective block POVM.

To improve on counting, at least one effective POVM effect must have an off-diagonal matrix element in that occupation basis. Off-diagonal effects are necessary, but not sufficient. A coherent interferometer before counting changes those effects; a measurement commuting only with total photon number need not be diagonal in the full occupation basis. Neither case is covered by this diagonal-record ceiling. The [two-photon example](qubit_optical_bridge.md) makes the single-mode distinction explicit.

## Energy-only upper bound

When $`c>0`$, use the residual $`J-aK/c`$. Its conditional mean given $`N=n`$ is zero, and multinomial second moments give

```math
\mathbb E[(J-aK/c)^2\mid N=n]=\frac{a(a+c)}c n.
```

Hence the residual has finite second moment even when $`\mathbb EN^2=\infty`$. Conditional expectation minimizes mean-square error, so

```math
\mathbb E\operatorname{Var}(J|K)
\le\frac{a(a+c)}c E.
```

For any integer random variable of variance $`v`$, adding an independent uniform variable on $`[-1/2,1/2]`$ and applying Gaussian maximal differential entropy gives $`H\le\frac12\log_2[2\pi e(v+1/12)]`$. Apply this conditionally and use Jensen's inequality. Since $`H(W|K)\ge0`$,

```math
Q_{\rm cnt}(E)\le U_E(E):=
\frac12\log_2\!\left[2\pi e\left(\frac{a(a+c)}c E+\frac1{12}\right)\right].
```

No variance or peak bound was imposed on the original photon distribution.

## A thinning identity for the loss-dependent converse

Let $`M=J+K`$ and $`T=W+K`$. Their distributions are $`T_{1-b}N`$ and $`T_{1-a}N`$. Given $`N`$, either pair $`(J,K)`$ or $`(W,K)`$ determines the full multinomial triple, so their conditional entropies are equal. Given $`M`$, the split into $`J,K`$ is independent of $`N`$; the analogous assertion holds for $`T`$. Therefore

```math
\begin{aligned}
H(J|K)-H(W|K)
&=I(N;M)-I(N;T)\\
&=H(T_{1-b}N)-H(T_{1-a}N)
 +\sum_n p_n[h_n(a)-h_n(b)].
\end{aligned}
```

This exact identity is useful because the first entropy difference is bounded independently of the input law.

### Thinning cannot reduce entropy by more than its log retention

For $`0<t\le1`$, the thinning transition matrix is $`P_{mn}=\binom nm t^m(1-t)^{n-m}`$. Its column sums are one and each row sums to $`1/t`$. Thus $`tP_{mn}`$, as a function of $`n`$ at fixed $`m`$, is a probability distribution. Nonnegativity of the relative entropy of the posterior $`p(n|m)`$ to that distribution gives, after averaging over $`m`$,

```math
H(T_tN)-H(N)\ge\log_2t.
```

Finite mean makes all entropies finite. The identity also follows by finite truncation and passage to the limit. Applying it to the composition of retentions $`1-b`$ and $`(1-a)/(1-b)`$ gives

```math
H(T_{1-b}N)-H(T_{1-a}N)
\le\log_2\frac{1-b}{1-a}.
```

### Uniform binomial entropy bounds

For $`v=nt(1-t)`$,

```math
\frac12\log_2(1+v)\le h_n(t)
\le\frac12\log_2[2\pi e(v+1/12)].
```

The upper bound is the preceding integer-variance inequality. Here is a direct proof of the lower bound. Parseval's identity expresses the collision probability as

```math
C=\frac1{2\pi}\int_{-\pi}^{\pi}
[1-4t(1-t)\sin^2(x/2)]^n\,dx.
```

It is at most the integral of $`e^{-4v\sin^2(x/2)}`$. For $`0\le v\le1/4`$, convexity puts this exponential below its chord as a function of $`\sin^2(x/2)`$, giving

```math
C\le(1+e^{-4v})/2\le1-2v+4v^2\le1-v\le(1+v)^{-1/2}.
```

For $`v\ge1/4`$, use $`\sin(|x|/2)\ge |x|/\pi`$ and extend the Gaussian integral to the line:

```math
C\le\frac{\sqrt\pi}{4\sqrt v}\le(1+v)^{-1/2}.
```

The last inequality follows from $`\pi<16/5`$. Shannon entropy is at least collision entropy, proving the claim, including $`v=0`$.

For $`b>0`$, these bounds imply, for every integer $`n\ge0`$,

```math
h_n(a)-h_n(b)
\le\frac12\log_2\!\left[
2\pi e\max\!\left\{\frac1{12},\frac{a(1-a)}{b(1-b)}\right\}\right].
```

Combining with thinning yields the input-uniform plateau bound

```math
Q_{\rm cnt}(E)\le U_b:=
\log_2\frac{1-b}{1-a}
+\frac12\log_2\!\left[
2\pi e\max\!\left\{\frac1{12},\frac{a(1-a)}{b(1-b)}\right\}\right].
```

Set $`U_b=\infty`$ at $`b=0`$. Together with the collective benchmark, the available counting upper bound is $`\min\{Q_{\rm coll},U_E,U_b\}`$, omitting $`U_E`$ when $`c=0`$. The constants are not claimed optimal.

## Thermal average input supplies the lower bound

Choose any mean $`0<X\le E`$ and a geometric input photon distribution, corresponding to a thermal average state. The collected count is geometric with mean $`cX`$. Conditional on $`K=k`$, the receiver count has the negative-binomial distribution equal to the sum of $`r=k+1`$ independent geometric variables, each of mean

```math
\mu=\frac{aX}{1+cX},\qquad w=\mu(1+\mu).
```

Equivalently,

```math
\Pr(J=j,K=k)=\binom{j+k}{j}
\frac{(aX)^j(cX)^k}{[1+(a+c)X]^{j+k+1}}.
```

For $`r`$ geometric summands, Parseval gives collision integral

```math
C_r=\frac1{2\pi}\int_{-\pi}^{\pi}
[1+4w\sin^2(x/2)]^{-r}\,dx
\le\frac{\sqrt\pi}{4\sqrt w}\frac{\Gamma(r-1/2)}{\Gamma(r)}
\le\frac{\pi}{4\sqrt{wr}}.
```

The first inequality uses the same sine bound and extends the integral to the line. For integer $`r\ge1`$, the second follows from $`\sqrt r\,\Gamma(r-1/2)/\Gamma(r)\le\sqrt\pi`$: it holds at one, and the ratio of consecutive terms has square $`1-3/(4r^2)+1/(4r^3)\le1`$. Thus

```math
H(J|K=k)\ge\frac12\log_2[(k+1)w]+\log_2(4/\pi).
```

For a geometric $`K`$ with maximum point probability $`p=1/(1+cX)`$, $`\Pr(K+1<t)\le pt`$. Integrating the lower tail of $`\ln(K+1)`$ yields

```math
\mathbb E\log_2(K+1)\ge\log_2(1+cX)-\log_2e.
```

Explicitly, $`\mathbb E[\ln((1/p)/(K+1))]_+\le\int_0^\infty e^{-s}ds=1`$. Finally $`H(W|K)\le H(W)=g(bX)`$. The counting capacity therefore obeys the finite lower bound

```math
Q_{\rm cnt}(E)\ge\max\{0,B(X)\},
```

```math
B(X)=\frac12\log_2[(1+cX)\mu(1+\mu)]
+\log_2(4/\pi)-\frac12\log_2e-g(bX).
```

This is an achieved coherent-information lower bound, not a claim that a thermal input is exactly optimal at finite energy. Energy-constrained coding justifies it; thermal truncations approach it with strict energy slack. The entropy of the omitted thermal tail vanishes by the same mixture bounds used in the [operational account](capacity_reduction.md). No infinite-support measurement is required at any finite approximating stage.

Choosing $`X=\min\{E,1/b\}`$ proves the lower half-logarithmic law; [Uniform laws](uniform_laws.md) gives the domain and constants' dependence.
