# Capacity with a mean reference-energy budget

[Model](model.md) · [Local conservation contract](reference_width_bounds.md#the-operation-constraint-is-separate-local-invariance) · [Direct construction](direct_reference.md)

Mean reference energy alone controls capacity under separate number conservation
at each collected mode. A first-absolute-moment estimate handles references with
arbitrarily large or infinite number variance. Together with the finite sine
construction, it determines the energy-driven capacity profile to an additive
constant and matches the linear initial reference stock needed for a bounded
rate gap.

## Resources and capacity

Use exactly the separate-local-invariance and independent-initial-reference
contract in the [spread converse](reference_width_bounds.md). In particular,
the effective helper effects satisfy

```math
[E_y,N_{D_i}+N_{W_i}]=0\quad\text{for every }y,i.
```

Each physical reference number operator has nonnegative integer spectrum. Its
zero is the physical ground level; a large offset is charged. Include every
number-bearing apparatus resource in this constraint. The reference systems may
be mixed or correlated with one another, but their joint initial state is
independent of the entire encoded signal and its logical reference. No associated
purification or entangled resource is supplied to the sender or receiver.

Let $`Q_{\rm loc}^{\rm mean}(E,M)`$ allow arbitrary endpoint block codes,
unrestricted classical helper records, mean signal budget $`E`$, and

```math
\frac1n\sum_i\langle N_{W_i}\rangle\le M.
```

This is an average initial stock constraint. There is no reference support,
variance, or maximum-energy assumption. General effects commuting only with the
sum of the local totals and coherent reuse of a signal-correlated reference
remain outside this contract.

## An all-code bound using only first moments

For $`a>b\ge0`$ and $`c=1-a-b>0`$, put

```math
A=\frac{a(a+c)}c,\qquad r=\frac ac.
```

Then

```math
\boxed{
Q_{\rm loc}^{\rm mean}(E,M)\le
\min\!\left\{Q_{\rm coll}(E),\,
\log_2\!\left[2e\left(\sqrt{AE}+rM+\frac14\right)\right]\right\}.
}
```

The collective benchmark is inherited from Partial Monitoring. Independent
helper ancillas do not enlarge its unrestricted measurement class. The second
bound is a weak capacity converse and covers coherent inputs, correlations
across channel uses, and discarded encoder ancillas.

Refine the helper record by every conserved local total, as in the
[spread proof](reference_width_bounds.md#refine-the-record-without-assuming-a-classical-input).
With $`J_i`$ the receiver number and $`T_i=D_i^{\#}+W_i^{\#}`$ the refined
total, that argument gives, for the actual logical reference $`R`$,

```math
I(R\rangle B^nY)\le\sum_i H(J_i|T_i).
```

Here the symbols $`D_i^{\#},W_i^{\#}`$ denote number random variables, not
replacement of the fine detector by a classical one. Only the commuting
$`(J_i,T_i)`$ marginal has its premeasurement number law. It is the convolution
of the optical number law and the independent reference number law.

For mean input energy $`E_i`$, the optical multinomial residual obeys

```math
\mathbb E\!\left[(J_i-rD_i^{\#})^2\mid N_i\right]=AN_i,
\qquad
\mathbb E|J_i-rD_i^{\#}|\le\sqrt{AE_i}.
```

The conditional residual has zero mean. Evaluate its second moment at each
input number before averaging, so that no input second moment is assumed.
Writing $`M_i=\mathbb E W_i^{\#}`$ and using nonnegative reference number,

```math
\mathbb E|J_i-rT_i|\le\sqrt{AE_i}+rM_i.
```

To convert this estimate into an entropy bound, introduce an independent
mathematical dither $`U_i`$, uniform on $`[-1/2,1/2]`$. This variable is a
proof device and consumes no apparatus resource. At each fixed $`T_i=t`$,
the unit intervals centered at the different integer values of $`J_i`$ are
disjoint. Translation by $`rt`$ therefore gives the exact identity

```math
h(J_i+U_i-rt\mid T_i=t)=H(J_i\mid T_i=t).
```

For any continuous random variable $`X`$ of mean absolute value $`m`$, the
Laplace density $`(2m)^{-1}e^{-|x|/m}`$ and relative-entropy positivity give
$`h(X)\le\log_2(2em)`$. Apply this conditionally and then use Jensen:

```math
\begin{aligned}
H(J_i|T_i)
&\le\log_2\!\left[2e\,\mathbb E|J_i+U_i-rT_i|\right]\\
&\le\log_2\!\left[2e\left(\sqrt{AE_i}+rM_i+\frac14\right)\right].
\end{aligned}
```

These are standard entropy tools; see Rioul,
[Variations on a Theme by Massey](https://arxiv.org/abs/2102.04200v4),
Theorem 1 and Theorem 4 at moment order one. No new general entropy inequality
is claimed. For countable number distributions, finite first moments ensure
finite discrete entropy by the geometric maximum-entropy bound. The conditional
dither identities are consequently legitimate entropy averages. Their mean
absolute values are at least $`1/4`$, so the logarithm has no singularity.
No difference of infinite record entropies is taken.

Finally, log concavity and Cauchy--Schwarz give

```math
\begin{aligned}
I(R\rangle B^nY)
&\le n\log_2\!\left[2e\left(
\frac1n\sum_i\sqrt{AE_i}+\frac rn\sum_iM_i+\frac14\right)\right]\\
&\le n\log_2\!\left[2e\left(\sqrt{AE}+rM+\frac14\right)\right].
\end{aligned}
```

Decoder data processing and the finite-logical-reference continuity bound in the
[record converse](detector_resources.md#a-matching-lower-bound-on-the-helper-record)
convert this inequality into the displayed capacity bound as unconditional
entanglement error vanishes. It holds under average resource constraints even
when individual uses have different signal and reference budgets.

## The complete mean-energy profile

Fix $`0\lt a\lt 1`$ and restrict to the energy-driven uniform domain

```math
E\ge1,\qquad
0\le b\le\tfrac12\min\{a,1-a\},\qquad bE\le1.
```

Here $`L=E`$ and $`c\ge(1-a)/2`$. Uniformly over this domain and all
$`M\ge0`$,

```math
\boxed{
Q_{\rm loc}^{\rm mean}(E,M)
=\min\!\left\{\log_2E,
\max\!\left\{\tfrac12\log_2E,\log_2(M+1)\right\}\right\}+O_a(1).
}
```

For the upper side, $`A`$ and $`r`$ are bounded by constants depending only
on $`a`$. The first-moment ceiling is therefore
$`\log_2(\sqrt E+M+1)+O_a(1)`$, which differs from the inner maximum by
at most a constant. The inherited collective ceiling supplies the outer minimum.

For the lower side, counting uses the vacuum reference and achieves
$`\tfrac12\log_2E-O_a(1)`$ by the [uniform counting law](uniform_laws.md).
When $`M\ge12`$, also use the direct coherent construction with

```math
x=\min\{E,M/12\}\ge1,\qquad
d=\lceil x\rceil+1,\qquad K=4d.
```

Choose the smallest odd prime $`q\ge d`$, so $`q<2d`$, and let $`h=q-1`$.
The initial sine reference has exact mean

```math
\langle N_W\rangle=h+\frac{K-1}{2}<4d\le12x\le M.
```

The truncated thermal signal has strict mean slack $`x_d\lt x\le E`$, tail
less than $`1/2`$, and $`bx\le1`$. The
[finite-cutoff bound](detector_resources.md#the-finite-record-tradeoff-to-an-additive-constant)
is at least $`\log_2x+\log_2a-4`$. Moreover,
$`(d-1)/(K+1)<1/4`$, so the
[actual discarded-reference penalty](direct_reference.md#entropy-of-a-mixture-of-translated-sine-references)
is at most $`g(3\pi^2/64)`$. Since $`M/12\ge(M+1)/13`$, this branch gives

```math
Q_{\rm loc}^{\rm mean}(E,M)\ge
\max\!\left\{0,\min\{\log_2E,\log_2(M+1)\}-C_a^{\rm mean}\right\},
\qquad
C_a^{\rm mean}=4+\log_2(13/a)+g(3\pi^2/64).
```

For $`M<12`$ the same displayed lower bound follows from zero rate because
$`C_a^{\rm mean}>\log_2 13`$. Taking the better of this branch and counting
proves the profile. The lower bound uses fresh independent references and a
predetermined measurement on each mode; the converse permits the larger class
specified above.

## Necessary stock and the role of rare high levels

If an attainable rate is at least $`\log_2E-C_0`$, the finite bound implies

```math
M\ge\frac ca\left[
\frac{2^{-C_0}E}{2e}-\sqrt{\frac{a(a+c)}cE}-\frac14\right].
```

Thus a bounded additive gap to the full logarithmic rate in the stated domain
requires average initial reference mean $`\Omega_a(E)`$. The direct construction
supplies $`O_a(E)`$ stock at fixed rate tolerances. Linear initial mean stock
is therefore the matching order for retaining the full rate within an
energy-independent additive constant in this operation class.

For example, a reference assigning probability $`1/m`$ to level $`m`$ and
the remainder to zero has mean one and variance $`m-1`$. Such a family defeats
an inference from variance to mean, but the first-moment bound above still gives
only $`\tfrac12\log_2E+O_a(1)`$, uniformly in $`m`$. Rare arbitrarily distant
levels cannot evade this mean-stock converse.

If $`\log_2(M+1)=\alpha\log_2E+O(1)`$ for fixed $`\alpha\ge0`$, the leading
rate coefficient is $`\min\{1,\max\{1/2,\alpha\}\}`$. Leading coefficient
one alone is weaker than a bounded additive gap; for example, $`M=E/\log E`$
has coefficient one but an unbounded necessary additive loss by the finite
upper bound.

This prices prepared reference photons, rather than preparation work, net
consumption, reset cost, or repeated use. The finite bound contains the actual
allowed signal energy $`E`$; it does not establish a matching uniform
mean-stock necessity in the loss-dominated regime $`E\gg L`$. Classical
records are unrestricted, so the profile does not optimize a simultaneous record
and reference budget.

## Verification

```bash
python -m unittest discover -s verification -p 'test_reference_mean.py' -v
```

The tests check actual coherent-input invariant detector channels, the
conditional entropy and first-moment bounds, sparse high-level reference tails,
averaging of unequal resource budgets, and the explicit attainable construction.
The written proof establishes the arbitrary-input and asymptotic claim; finite
tests do not replace it.
