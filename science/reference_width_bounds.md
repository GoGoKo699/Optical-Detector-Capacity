# A capacity bound from local reference number spread

[Model](model.md) · [Direct finite-reference detector](direct_reference.md) · [Apparatus contract](finite_reference.md#apparatus-contract)

A detector reference with bounded photon-number spread limits the communication
rate under separate number conservation at each collected mode. The bound covers
arbitrary coherent inputs, correlated endpoint codes, and discarded encoder
ancillas. It requires neither input phase twirling, reference purity, nor a
degradability assertion about the actual detector. In the energy-driven regime,
it supplies a support-width converse to the direct finite-reference construction.
Its variance argument alone cannot lower-bound reference mean energy. The
[separate first-moment proof](reference_mean_bounds.md) gives the matching
mean-stock converse under this same operation contract.

## The operation constraint is separate local invariance

Assume $`a>b\ge0`$, $`c>0`$ and $`a+b+c=1`$. For an $`n`$-use code, the helper
has collected modes $`D_i`$ and reference systems $`W_i`$ with integer number
operators. The initial reference state is independent of the entire encoded
signal and its logical reference. The $`W_i`$ may be mixed or mutually
correlated; the sender and receiver hold no purification or additional entangled
resource associated with them. The effective helper POVM obeys

```math
[E_y,T_i]=0\quad\text{for every }y,i,
\qquad T_i=N_{D_i}+N_{W_i}.
```

This includes predetermined individual-mode invariant measurements, their
classically adaptive choices, and joint effects obeying every separate
commutation relation. All other number-bearing apparatus resources at a mode
must be included in its reference and invariance contract. Classical processing
of the outcomes is unrestricted.

Commutation with only $`\sum_iT_i`$ is a larger class. The two-mode projector
onto $`(|10\rangle+|01\rangle)/\sqrt2`$, for example, commutes with total
number but not either local number. General globally conserving collective
measurements are outside the assertion. Reusing a reference after it becomes
correlated with signal systems is also not automatically covered by the stated
independent-initial-reference and separate-local-operator assumptions.

Suppose the reference number variances satisfy

```math
\frac1n\sum_i\mathrm{Var}(N_{W_i})\le V.
```

A bound $`V`$ on every reference suffices. If every reference is supported in an
interval of $`K`$ consecutive photon levels, possibly with different known
offsets, then $`V\le(K-1)^2/4`$. Offsets change mean reference energy but not
this variance bound.

## Capacity upper bound

Let $`Q_{\rm loc}(E,V)`$ denote capacity under this operation constraint, mean
signal budget $`E`$ per original mode, and the average variance bound. Arbitrary
endpoint encoders and decoders are allowed. Then

```math
\boxed{
Q_{\rm loc}(E,V)\le\min\!\left\{
Q_{\rm coll}(E),\,
\frac12\log_2\!\left[2\pi e\left(
\frac{a(a+c)}cE+\frac{a^2}{c^2}V+\frac1{12}
\right)\right]\right\}.
}
```

For a common width bound $`K`$, substitute $`V=(K-1)^2/4`$. The inherited
collective bound applies because independent reference ancillas are already
permitted in the unrestricted partial-monitoring model. The second bound is a
weak capacity converse, not an exact capacity or a strong-converse exponent.

## Refine the record without assuming a classical input

The commuting $`T_i`$ have joint projectors $`\Pi_{\mathbf t}`$. Refine the
effects to

```math
E_{y,\mathbf t}=\Pi_{\mathbf t}E_y\Pi_{\mathbf t}.
```

Invariance gives $`\sum_{\mathbf t}E_{y,\mathbf t}=E_y`$. Forgetting the new
label exactly reproduces the original receiver/reference channel for every
input. Providing $`Y=(y,\mathbf t)`$ can therefore only help the receiver and
is a valid converse relaxation. Rank-one refinement is unnecessary. Moreover,
$`\sum_yE_{y,\mathbf t}=\Pi_{\mathbf t}`$, so the receiver number $`J_i`$
and retained label $`T_i`$ have their premeasurement joint number distribution.

With the actual transmitted logical reference $`R`$, conditional subadditivity
and number dephasing give

```math
\begin{aligned}
I(R\rangle B^nY)
&=S(B^n|Y)-S(RB^n|Y)\\
&\le S(B^n|Y)\\
&\le\sum_iS(B_i|Y)\\
&\le\sum_iH(J_i|Y)
\le\sum_iH(J_i|T_i).
\end{aligned}
```

Here $`S(RB^n|Y)\ge0`$ because the conditioning record is classical. This
argument includes discarded encoder ancillas without treating them as part of
the logical reference. For countable or continuous records, use conditional
entropy averages, not a difference of potentially infinite $`S(B^nY)`$ and
$`S(RB^nY)`$. Finite logical dimension and mean signal energy bound the averaged
quantum entropies in the display. Normal instruments and standard Borel records
have the finite-partition interpretation in the
[operational reduction](capacity_reduction.md).

The fully resolved $`y`$ distribution can depend on input coherence. The proof
does not assume otherwise: only its coarser commuting pair $`(J_i,T_i)`$ is
replaced by the corresponding number distribution.

## A residual estimate using only the first signal moment

Let $`N_i`$ have the number distribution of the $`i`$th input marginal and mean
$`E_i`$. Denote its collected photon count by $`D_i^{\#}`$. The joint number
law is multinomial even for a coherent marginal input, giving

```math
\mathbb E\!\left[J_i-\frac acD_i^{\#}\,\middle|N_i\right]=0,
\qquad
\mathbb E\!\left[
\left(J_i-\frac acD_i^{\#}\right)^2\middle|N_i\right]
=\frac{a(a+c)}cN_i.
```

Set $`\mu_i=\mathbb E N_{W_i}`$. Initial reference independence and
$`T_i=D_i^{\#}+N_{W_i}`$ give the exact estimator error

```math
\mathbb E\!\left[
\left(J_i-\frac ac(T_i-\mu_i)\right)^2\right]
=\frac{a(a+c)}cE_i
+\frac{a^2}{c^2}\mathrm{Var}(N_{W_i}).
```

The cross term vanishes by independence. Derive the residual second moment
conditional on $`N_i`$ before averaging: no signal second-moment assumption was
made, so subtracting separately infinite second moments would be invalid. The
conditional mean minimizes square error, hence

```math
\mathbb E\,\mathrm{Var}(J_i|T_i)
\le\frac{a(a+c)}cE_i+\frac{a^2}{c^2}\mathrm{Var}(N_{W_i}).
```

For an integer random variable of variance $`v`$, independent uniform dithering
on $`[-1/2,1/2]`$ and Gaussian maximal differential entropy imply
$`H\le\tfrac12\log_2[2\pi e(v+1/12)]`$, the elementary estimate also used
in the [counting converse](counting_bounds.md). Apply it conditionally and use
Jensen's inequality over $`T_i`$ and over uses. Since $`\sum_iE_i\le nE`$,

```math
I(R\rangle B^nY)
\le\frac n2\log_2\!\left[2\pi e\left(
\frac{a(a+c)}cE+\frac{a^2}{c^2}V+\frac1{12}
\right)\right].
```

Decoder data processing and the finite-logical-reference continuity argument in
the [record converse](detector_resources.md#a-matching-lower-bound-on-the-helper-record)
give the capacity upper bound as unconditional entanglement error vanishes.
The proof treats arbitrary coherent and correlated inputs directly; it neither
twirls the input nor assumes an isometric encoder.

## Necessary spread in the energy-driven regime

If an attainable rate is at least $`\log_2E-C_0`$ for fixed $`C_0`$, then

```math
V\ge\frac{c^2}{a^2}\left[
\frac{2^{-2C_0}E^2}{2\pi e}
-\frac{a(a+c)}cE-\frac1{12}\right].
```

For fixed $`0<a<1`$ and bounded $`bE`$ as $`E\to\infty`$,
$`c=1-a-b\to1-a>0`$. A fixed additive gap to the full logarithmic rate
therefore requires average reference variance $`V=\Omega(E^2)`$. A common
per-use support-width bound must satisfy $`K=\Omega(E)`$. For nonuniform
widths the variance argument bounds the root-mean-square support span; it does
not give the same lower bound on their arithmetic average.

In particular, this applies to $`E=L=\min\{E,1/b\}`$ with $`bE\le1`$,
where $`Q_{\rm coll}(E)=\log_2E+O_a(1)`$. Fixed width gives at most a
one-half logarithmic upper coefficient. More generally, $`K=O(E^\alpha)`$
with $`0\le\alpha<1`$ gives upper coefficient $`\max\{1/2,\alpha\}`$.
A leading coefficient of one alone is weaker than a bounded additive gap and
does not by itself force $`K=\Omega(E)`$.

The [direct construction](direct_reference.md#a-linear-stock-of-prepared-reference-photons)
uses fresh independent sine references with $`K=O_\beta(d)`$ at fixed reference
penalty. Its fixed-tolerance cutoff has $`d=O(L+1)`$. Thus, when
$`E=L\to\infty`$, width $`O(E)`$ suffices and a common width
$`\Omega(E)`$ is necessary for the bounded-gap goal within this operation
class. This matches support-width scaling, not gate count or thermodynamic work.

The upper bound contains the actual allowed signal energy $`E`$. It does not
prove uniform width necessity $`\Omega(L)`$ when $`E\gg L`$, because the
signal term may dominate. It also does not convert spread into a universal mean
reference-energy bound: a number distribution assigning probability $`1/m`$ to
level $`m`$ and the remainder to zero has mean one and variance $`m-1`$.
Rare distant levels obstruct that inference. The
[first-moment converse](reference_mean_bounds.md) handles these states directly
and proves linear mean-stock necessity in the energy-driven regime without
inferring a mean bound from variance.

## The complete width profile to an additive constant

Let $`Q_{\rm loc}^{[K]}(E)`$ be the capacity in the separate-invariance class
above with a common bound of $`K\ge1`$ consecutive number levels for each
initial reference. Classical helper records are unrestricted in this profile.
Fix $`0<a<1`$ and use the energy-driven part of the original
[uniform domain](uniform_laws.md):

```math
E\ge1,\qquad 0\le b\le\tfrac12\min\{a,1-a\},\qquad bE\le1.
```

Then $`L=E`$ and $`c\ge(1-a)/2>0`$. Uniformly over these parameters and all
$`K\ge1`$,

```math
\boxed{
Q_{\rm loc}^{[K]}(E)
=\min\!\left\{\log_2E,
\max\!\left\{\tfrac12\log_2E,\log_2K\right\}\right\}+O_a(1).
}
```

This is an additive characterization, not an exact finite-energy capacity.
The upper bound permits every helper effect satisfying all the local
commutation relations, while the lower bound uses independent references and
predetermined individual-mode measurements.

For the upper side, the variance bound and $`V\le(K-1)^2/4`$ give
$`\tfrac12\log_2(E+K^2)+O_a(1)`$. The inherited collective bound gives
$`\log_2E+O_a(1)`$. Since the first expression differs from
$`\max\{\tfrac12\log_2E,\log_2K\}`$ by at most an additional one-half bit
apart from its stated constants, their minimum gives the displayed upper
profile.

For the lower side, ordinary counting uses no coherent reference and already
attains $`\tfrac12\log_2E-O_a(1)`$ throughout this domain. If $`K\ge4`$,
also consider the direct coherent detector at

```math
x=\min\{E,K/4\}\ge1,\qquad d=\lceil x\rceil+1,
```

with a sine reference of exactly $`K`$ initial number levels. Its normalized
truncated thermal input has mean strictly below $`x\le E`$ and retained mass
greater than $`1/2`$. Also $`bx\le1`$. The finite-cutoff estimate used in
the [record tradeoff](detector_resources.md#the-finite-record-tradeoff-to-an-additive-constant)
therefore gives an ideal bound of $`\log_2x+\log_2a-4`$.

For the actual reference, $`r=(d-1)/(K+1)\le1/2`$, so the
[conditional-reference entropy bound](direct_reference.md#entropy-of-a-mixture-of-translated-sine-references)
costs at most $`g(5\pi^2/48)`$. Hence the coherent branch achieves every
rate below a positive lower bound of

```math
\min\{\log_2E,\log_2K\}-C_a^{\rm ref},\qquad
C_a^{\rm ref}=6+\log_2(1/a)+g(5\pi^2/48).
```

Taking the better of counting and this coherent branch gives the lower
profile. For $`K\le3`$, the possible $`\log_2K`$ contribution is bounded
by $`\log_2 3`$ and is absorbed by the additive constant. No uncharged
phase reference or outcome postselection is used. The coherent construction's
initial mean reference is $`O(K+1)`$; only its support width is being
constrained in this profile.

For example, if $`\log_2K=\alpha\log_2E+O(1)`$ at fixed $`\alpha\ge0`$,
the leading rate coefficient is

```math
\min\{1,\max\{1/2,\alpha\}\}.
```

Widths up to order $`\sqrt E`$ retain counting's leading coefficient. The
coefficient increases between widths $`\sqrt E`$ and $`E`$, and reaches one
at linear width. A bounded additive gap requires the stronger width condition
already proved above; leading coefficient one by itself does not imply such a
gap. The corresponding [mean-energy profile](reference_mean_bounds.md) is proved
separately. Neither profile optimizes a simultaneous finite classical-record
and reference budget.

## Verification

```bash
python -m unittest discover -s verification -p 'test_reference_width.py' -v
```

The tests construct coherent encoded signals, independent mixed coherent
references, the full optical isometry, and random invariant sector measurements.
They check logical coherent information, refinement, the joint number law,
residual mean-square identity, and conditional entropy bound. A two-mode
projector distinguishes global from local conservation. The written argument
establishes arbitrary dimensions, heavy-tailed finite-mean inputs, and the code
converse; finite numerical checks do not replace it.
