# Detector records, cutoff, and control accuracy

[Model](model.md) · [Structured detector](coherent_measurements.md) · [Uniform laws](uniform_laws.md)

The selected quadratic-phase Fourier detector has a finite resource account. A cutoff
of order the useful signal energy suffices for a constant additive rate gap. Its
classical record has the optimal leading logarithmic size. A conditional-entropy
bound also gives sufficient implementation accuracy. These statements price
outcomes and mathematical control error; they do not determine a physical gate
count or the full energy cost of a phase reference.

Assume $`a>b\ge0`$ and $`0<a<1`$. Write $`x>0`$ for a chosen mean input energy,
$`d=M+1\ge2`$ for the input cutoff dimension, and $`q`$ for the smallest odd prime
at least $`d`$. The detector, including the selected quadratic setting, is chosen
before transmission from the known channel and average coded input.

## An explicit finite cutoff

Let $`\tau_x`$ be the thermal input of mean $`x`$, and put

```math
z=\frac{x}{1+x},\qquad t=z^d,\qquad
\tau_{x,d}=\frac{P_d\tau_xP_d}{1-t},\qquad
x_d=x-\frac{dt}{1-t}<x.
```

Here $`t`$ is discarded probability in constructing the average input; it is not
an operational failure probability. The normalized truncated state itself is used
as the average coded input, and all detector outcomes are retained.

Positivity gives $`\tau_{x,d}\le\tau_x/(1-t)`$. The splitter and partial traces
preserve this order. For positive operators $`A\le C`$,

```math
\mathrm{Tr}(C^2-A^2)=\mathrm{Tr}[(C-A)(C+A)]\ge0.
```

Consequently the finite receiver/joint-output purity sum obeys

```math
C_d:=\mathrm{Tr}\,\rho_{B,d}^2+\mathrm{Tr}\,\rho_{BD,d}^2
\le\frac{1}{(1-t)^2}
\left[\frac1{1+2ax}+\frac1{1+2(1-b)x}\right].
```

The inaccessible output has mean $`bx_d`$, so thermal maximal entropy gives
$`S(Z_d)\le g(bx_d)\le g(bx)`$. The [fixed-setting purity argument](coherent_measurements.md#one-predetermined-fourier-measurement-suffices)
therefore proves the finite-cutoff guarantee

```math
I_c\ge R_1(x)-\kappa(t),\qquad
\kappa(t)=-2\log_2(1-t),
```

where $`R_1`$ is the individual-mode lower bound already defined there. This
one-sided estimate needs no entropy-continuity approximation for the infinite
thermal tail.

For an additive cutoff tolerance $`\gamma>0`$, set

```math
\delta_\gamma=1-2^{-\gamma/2},\qquad
d=\max\!\left\{2,
\left\lceil\frac{\ln(1/\delta_\gamma)}{\ln(1+1/x)}\right\rceil\right\}.
```

Then $`t\le\delta_\gamma`$ and $`\kappa(t)\le\gamma`$. The simpler choice
$`d=\max\{2,\lceil(x+1)\ln(1/\delta_\gamma)\rceil\}`$ also suffices, since
$`\ln(1+1/x)\ge1/(x+1)`$. At every such fixed cutoff, code for the finite
flagged channel before increasing the cutoff. The strict energy slack
$`x_d<x\le E`$ preserves the original average signal-energy contract.

## Use the energy that still improves the rate

Take

```math
x=L:=\min\{E,1/b\},\qquad 1/0=\infty.
```

When $`E>L`$, put $`u=a/b>1`$. The inherited collective capacity is increasing
and has ceiling $`\log_2u`$. Since $`g(1)=2`$ and
$`g(u)-\log_2u=(u+1)\log_2(1+1/u)\ge\log_2e`$,

```math
Q_{\rm coll}(E)-Q_{\rm coll}(L)
\le \log_2u-g(u)+2\le2-\log_2e.
```

The selected finite detector thus achieves a rate within $`2+\gamma`$ of
$`Q_{\rm coll}(E)`$. If $`E=L`$, the tighter gap is $`\log_2e+\gamma`$.
As always, negative displayed lower bounds are replaced by zero, and coding
attains every rate strictly below a positive coherent-information bound.

For $`0<\gamma\le1`$ this uses

```math
d=O((L+1)\ln(2/\gamma)),\qquad q<2d.
```

The record alphabet has $`q`$ coded outcomes, or $`q+1`$ symbols if the outside
outcome is included. Fixed-length transmission uses at most
$`\lceil\log_2(q+1)\rceil`$ bits per original mode. At any fixed additive
tolerance this is $`\log_2L+O(1)`$ for $`L\ge1`$. The predetermined quadratic
setting is part of the apparatus specification, not an additional transmitted
label.

## A matching lower bound on the helper record

This subsection deliberately prices a resource that the base model supplies
without limit. Let $`Q(E,r_c)`$ denote the best unconditional transmission rate
when the entire classical helper-to-receiver transcript $`Y`$ of an $`n`$-use
code satisfies $`H(Y)\le nr_c+o(n)`$. Here $`Y`$ is finite or countable and
$`H`$ is discrete Shannon entropy; a continuous detector record must be encoded
into an actual message before imposing this budget. A fixed-length alphabet of size at most
$`2^{nr_c+o(n)}`$ is sufficient for this entropy constraint. The helper may
measure collectively. The sender receives no feedback and shares no initial
entanglement with the helper or receiver. Settings scheduled in advance are
known constants; any additional announced setting belongs to $`Y`$.

Let

```math
Q_0(E)=\max\{0,g(aE)-g((1-a)E)\}.
```

This is the established unassisted pure-loss capacity, stated and proved in
[Wilde and Qi, Eq. (1) and Section X.A](https://arxiv.org/pdf/1609.01997v2).
Then

```math
Q(E,r_c)\le\min\{Q_{\rm coll}(E),\ Q_0(E)+r_c\}.
```

To prove the second bound, use $`R`$ for the transmitted reference. Discarding
the classical helper outcome leaves exactly the unmeasured $`RB^n`$ state:
local processing at the helper cannot signal to it. The conditional mutual
information identity and the fact that $`Y`$ is classical give

```math
I(R\rangle B^nY)-I(R\rangle B^n)
=I(R;Y|B^n)
=S(Y|B^n)-S(Y|RB^n)\le H(Y).
```

The unmeasured receiver channel is pure loss of fraction $`a`$. For
$`a\le1/2`$ it is antidegradable: $`RB^n`$ has a symmetric receiver extension.
Weak monotonicity gives $`S(R|B^n)\ge0`$, even if the encoder discarded an
ancilla. Hence $`I(R\rangle B^n)\le0`$.

For $`a>1/2`$, purify the encoded state as $`RFA^n`$, where $`F`$ is the
discarded encoder ancilla, and write $`C`$ for the entire unmeasured loss output.
After the splitter,

```math
I(R\rangle B^n)
=I_c(\rho_{A^n},\mathcal L_a^{\otimes n})-S(F|C).
```

Degradability produces another $`C'`$ from $`B^n`$ with the same $`FC`$
marginal. Weak monotonicity on $`FCC'`$ gives $`S(F|C)\ge0`$. Additivity of
degradable-channel coherent information, the pure-loss optimum, and its concavity
in the energy budget then bound the right side by $`nQ_0(E)`$. This step keeps
arbitrary correlated inputs, nonuniform mode energies, and discarded encoder
ancillas in the converse. The entropy expressions are finite: the signal budget
gives $`S(A^n)\le ng(E)`$, and
$`S(F)=S(RA^n)\le\log_2K+ng(E)`$; the loss output also has finite mean energy.

Finally, if a decoded code of dimension $`K`$ has half trace-distance error
$`\epsilon_n`$ from the maximally entangled target, decoder data processing and
Winter's conditional-entropy bound imply

```math
(1-2\epsilon_n)\log_2K
-(1+\epsilon_n)h_2\!\left(\frac{\epsilon_n}{1+\epsilon_n}\right)
\le nQ_0(E)+H(Y).
```

Divide by $`n`$ and take $`\epsilon_n\to0`$. This proves the rate bound.
The argument is an application of established entropy, degradability, and
pure-loss capacity results, rather than a new general information inequality.
It is a weak converse, not a strong-converse error exponent.

For every fixed $`0<a<1`$, $`Q_0(E)`$ is bounded independently of $`E`$:
it vanishes for $`a\le1/2`$ and is at most
$`\log_2[a/(1-a)]`$ otherwise. Therefore reaching
$`\log_2L-O_a(1)`$ qubits per mode requires
$`r_c\ge\log_2L-O_a(1)`$. The finite detector above supplies
$`r_c\le\log_2L+O(1)`$ at fixed additive tolerance. The leading helper record
cost is consequently necessary and sufficient. An exact finite-energy frontier
remains open; the following bounds characterize it to an additive constant.

## The finite record tradeoff to an additive constant

The same construction gives a uniform additive characterization throughout the
record budget. Assume $`a>b\ge0`$, fixed $`0<a<1`$, $`L=\min\{E,1/b\}\ge1`$
and $`r_c\ge0`$. Define constants depending only on the received fraction,

```math
C_a=7+\log_2(1/a),\qquad
k_a=\max\{0,\log_2[a/(1-a)]\},\qquad
D_a=\max\{k_a,g(a)\}.
```

Then

```math
\boxed{
\begin{aligned}
\max\{Q_0(E),\ \min\{r_c,\log_2L\}-C_a\}
&\le Q(E,r_c)\\
&\le\min\{Q_{\rm coll}(E),Q_0(E)+r_c\}\\
&\le\min\{r_c,\log_2L\}+D_a.
\end{aligned}}
```

The lower bound uses one predetermined individual-mode detector; the upper bound
permits collective helper measurements and arbitrary endpoint codes. These are
additive bounds, not an exact finite-energy capacity formula. The constants are
explicit conservative choices, rather than optimized detector overheads.

For $`r_c\ge3`$, spend only the useful energy compatible with the record:

```math
x=\min\{L,2^{r_c-3}\}\ge1,\qquad
M=\lceil x\rceil,\qquad d=M+1.
```

Use the normalized thermal state of mean $`x`$ truncated to $`0,\ldots,M`$.
Its retained mass $`p=1-[x/(1+x)]^d`$ is greater than $`1/2`$: Bernoulli's
inequality gives $`(1+1/x)^d\ge1+d/x>2`$. The input mean is strictly below
$`x\le L\le E`$, so there is signal-energy slack for coding. Also $`bx\le1`$.
The positive-operator estimate from the finite-cutoff argument gives

```math
C_d\le\frac1{p^2}
\left[\frac1{1+2ax}+\frac1{1+2(1-b)x}\right]
\le\frac4{ax},\qquad
S(Z_d)\le g(bx)\le2.
```

Here $`1-b\ge a`$ was used. The selected quadratic-phase Fourier detector
therefore has coherent information

```math
I_c\ge-\log_2C_d-S(Z_d)
\ge\log_2x+\log_2a-4
\ge\min\{r_c,\log_2L\}-C_a.
```

Its smallest odd prime $`q\ge d`$ satisfies $`q<2d`$. Including the outside
outcome in the alphabet still leaves strict record-rate slack:

```math
q+1<2x+5\le7x\le\frac78\,2^{r_c}.
```

The selected setting is fixed and known before transmission. Every $`n`$-symbol
transcript can be encoded injectively in
$`\lceil n\log_2(q+1)\rceil`$ bits, which is at most $`nr_c`$ for sufficiently
large $`n`$. This is lossless encoding of the entire transcript; rounding each
symbol separately to $`\lceil\log_2(q+1)\rceil`$ bits is unnecessary. It also
directly meets the Shannon budget since $`H(Y)\le n\log_2(q+1)<nr_c`$.
No record distribution assumption or omitted outcome is needed for this bound.
The outside outcome has zero probability on the code support, but is included
in the alphabet estimate anyway.

For $`r_c<3`$, $`\min\{r_c,\log_2L\}-C_a<0`$, and the no-helper scheme
suffices for that part of the bound. The no-helper capacity $`Q_0(E)`$ is
achievable at every budget. Taking the better of the no-helper scheme and the
fixed detector proves the lower maximum without requiring time sharing.

For the last upper inequality, $`Q_0(E)\le k_a`$. If $`L=E\ge1`$, then
$`g(aE)-\log_2E`$ decreases with $`E`$, so
$`Q_{\rm coll}(E)\le g(aE)\le\log_2L+g(a)`$. If $`L=1/b\le E`$, the
loss ceiling gives $`Q_{\rm coll}(E)\le\log_2(a/b)\le\log_2L`$. These two
cases, including $`b=0`$ in the first, combine with the record converse.

Thus, uniformly over $`r_c\ge0`$ and $`L\ge1`$ at fixed $`a`$,

```math
Q(E,r_c)=\min\{r_c,\log_2L\}+O_a(1).
```

In particular, if $`r_c=\alpha\log_2L+O(1)`$ for fixed $`\alpha\ge0`$,
the leading rate is $`\min\{\alpha,1\}\log_2L+O_a(1)`$, with the bounded
budget offset included in the additive constant. The statement prices the
transmitted classical record; it does not price coherent control, a phase
reference, apparatus energy, or decoder complexity.

## Sufficient control accuracy

Fix the truncated average input and purify it with a reference of dimension at
most $`d`$. Let $`\Phi`$ be the ideal flagged channel and $`\widetilde\Phi`$
the actually implemented fixed memoryless channel. The implementation acts only
on the helper. Both outputs contain the receiver and the full classical record,
including an outside outcome, in a common finite alphabet after relabeling.
The receiver retains finite photon support, so the coding theorem's finite-output
entropy conditions hold. Suppose

```math
\frac12\left\|(\mathrm{id}_R\otimes\Phi)(\psi)
-(\mathrm{id}_R\otimes\widetilde\Phi)(\psi)\right\|_1\le\varepsilon\le1.
```

A half diamond-distance bound on the allowed input subspace is sufficient, but
only this fixed-input bound is needed for the construction. With

```math
w_d(\varepsilon)=2\varepsilon\log_2d
 +(1+\varepsilon)h_2\!\left(\frac{\varepsilon}{1+\varepsilon}\right),
```

[Winter's Lemma 2](https://arxiv.org/pdf/1507.07775v6), applied to
$`-S(R|BY)`$, gives

```math
I_c(\tau_{x,d},\widetilde\Phi)
\ge R_1(x)-\kappa(t)-w_d(\varepsilon).
```

Coding for the actual channel attains every rate below a positive right side.
The conditioning system contains a quantum receiver, so the coefficient of
$`\varepsilon\log_2d`$ is two. This formulation automatically includes
unobserved apparatus degrees of freedom and a copied classical record. After
noisy coarse graining, subtracting only the old $`Z`$ entropy could omit part of
the true complement and would not justify this rate bound.

For the ideal unitary $`U=\mathcal F_qD_s`$, an implementation with
$`\|\widetilde U-U\|\le\varepsilon`$ on the occupied input subspace gives
the required trace-distance bound by contraction under measurement and partial
trace. For example, let $`\varepsilon_F`$ bound the Fourier operator error,
and let the diagonal phase differ by $`\Delta\theta k+\Delta\chi k^2`$ on
$`k<d`$, in radians. A sufficient bound is

```math
\varepsilon_F+|\Delta\theta|(d-1)
 +|\Delta\chi|(d-1)^2\le\varepsilon\le1.
```

For independent per-use random phase errors, averaging the corresponding
operator-error bound also suffices. A separate readout error must be included in
the channel distance; for example, independent classical erasure of probability
$`\xi`$ adds at most $`\xi`$ to its bound. Correlated adversarial drift across a
whole code block is outside this fixed-memoryless-channel statement.

An explicit sufficient choice for an additional rate tolerance $`0<\beta\le1`$ is

```math
\varepsilon=\frac{\beta}{4\log_2(8d/\beta)}.
```

Indeed, $`(1+\varepsilon)\ln(1+\varepsilon)\le2\varepsilon`$ for
$`0\le\varepsilon\le1`$, so
$`w_d(\varepsilon)\le\varepsilon[2\log_2d+\log_2(1/\varepsilon)+2\log_2e]\le\beta`$
for this choice. Combining it with the cutoff tolerance $`\gamma`$ gives a
finite detector within $`2+\gamma+\beta`$ of the full-energy collective
benchmark. Splitting the operator-error budget into thirds, for example, permits
$`\varepsilon_F\le\varepsilon/3`$,
$`|\Delta\theta|\le\varepsilon/[3(d-1)]`$, and
$`|\Delta\chi|\le\varepsilon/[3(d-1)^2]`$ before any additional readout error.

In the [uniform energy/loss domain](uniform_laws.md), at fixed received fraction
and cutoff tolerance, $`d=O(L+1)`$. A constant implementation error
$`\varepsilon<1/4`$ therefore still certifies a leading rate at least
$`(1-2\varepsilon)\log_2L-O_{a,\varepsilon}(1)`$, strictly above counting's
half-logarithmic coefficient. To retain a fixed additive gap using this continuity
estimate, $`\varepsilon=O(1/\log d)`$ suffices. The displayed phase bound then
allows linear-phase errors of order $`1/(d\log d)`$ and quadratic-phase errors
of order $`1/(d^2\log d)`$, with appropriate constants and Fourier accuracy.
These are sufficient accuracy conditions, not precision lower bounds or a
physical synthesis-cost theorem.

## Excitation transferred by this Fourier stage

For the truncated thermal average input, the helper marginal before control is
number diagonal with mean $`cx_d`$. The quadratic phase preserves it. A Fourier
transform on the first $`q`$ levels maps its diagonal probabilities to the
uniform distribution. Immediately before counting,

```math
\langle\hat n_D\rangle_{\rm after}=\frac{q-1}{2},\qquad
\Delta\langle\hat n_D\rangle=\frac{q-1}{2}-cx_d\ge0.
```

The last inequality uses the decreasing truncated-geometric input probabilities,
which give $`x_d\le(d-1)/2`$, and $`q\ge d`$. For an oscillator Hamiltonian
$`\hbar\omega\hat n_D`$, the displayed change corresponds to
$`\hbar\omega\Delta\langle\hat n_D\rangle`$ of mean oscillator energy.
This is an account of the specified ideal Fourier stage on its average input.
It is not a universal detector energy lower bound and excludes reference
preparation, reset, discarded apparatus systems, and control synthesis. The
base signal budget still counts incident photons only. The
[finite-reference realization](finite_reference.md) supplies this stage by an
exactly conserving joint control, prices a finite initial reference stock, and
tracks the corresponding energy transfer. Preparing and resetting that stock
and synthesizing the control are separate costs.

## Verification

Run the finite resource checks alongside the existing suites:

```bash
python -m unittest discover -s verification -p 'test_*.py' -v
```

The resource tests check finite cutoff inequalities, full-reference noisy
instruments, transcript entropy bounds, and the specified Fourier excitation
change. The written arguments establish the arbitrary-code converse and the
asymptotic scaling; a finite parameter grid is not a substitute for those proofs.
