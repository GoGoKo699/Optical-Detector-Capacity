# Where the qubit counting optimum first breaks

[Model](model.md) · [Operational reduction](capacity_reduction.md) · [Coherent detector](coherent_measurements.md)

The partial-monitoring qubit theorem proves that photon counting is optimal among
all predetermined individual helper POVMs when each input is supported on vacuum
and one photon. The optical result permits more photon numbers and finds a different
answer. A two-photon cutoff already separates the two detector classes: it does not
require the high-energy limit or the large coherent POVM used in the uniform bounds.

The detector below has a direct antecedent: Memarzadeh, Cafaro, and Mancini,
[Quantum information reclaiming after amplitude damping](https://arxiv.org/pdf/1004.0497),
Section 4.2, Eqs. (41)–(42) and (52)–(54), mix the vacuum and two-photon environmental
outcomes while keeping the one-photon outcome fixed. Their comparison concerns
one-use corrected entanglement fidelity with full environmental access. That
detector and its qualitative qubit/qutrit contrast are inherited. The comparison
here instead certifies an unconditional communication rate above the capacity of
every counting code when some loss remains inaccessible.

This page concerns an **additional per-mode photon cutoff**. Every encoder output is
supported on the tensor power of

```math
\mathcal H_2=\mathrm{span}\{|0\rangle,|1\rangle,|2\rangle\}.
```

Sender and receiver block codes remain unrestricted within that support. This is
stronger than an average-energy constraint. The counting upper bound below is not
an upper bound for full-Fock counting with only a mean-energy budget.

## A finite separation

Fix the same split used for the qubit comparison,

```math
(a,b,c)=\left(\frac15,\frac2{25},\frac{18}{25}\right).
```

Let $`Q_{\rm cnt}^{[2]}`$ be the counting capacity under the per-mode cutoff. The
following fixed projective detector on the occupied helper support, followed by
ordinary endpoint coding, has an achievable rate $`R_{\pm}^{[2]}`$ satisfying

```math
Q_{\rm cnt}^{[2]}<0.318,
\qquad
R_{\pm}^{[2]}>0.329,
\qquad
R_{\pm}^{[2]}-Q_{\rm cnt}^{[2]}>0.011
```

in qubits per original channel use. The detector basis and average input are

```math
\left\{|1\rangle,\frac{|0\rangle+|2\rangle}{\sqrt2},
\frac{|0\rangle-|2\rangle}{\sqrt2}\right\},
\qquad
\rho=\frac12|1\rangle\langle1|+\frac12|2\rangle\langle2|.
```

Add $`I-P_{\mathcal H_2}`$ as a fourth effect to define a complete detector on the
full Fock space. Its probability is zero under the stated input cutoff. All occupied
outcomes are retained; the rate is unconditional, with no postselection or sender
feedback. The average input is that of a quantum code, not a classical-number-state
communication protocol. The detector requires coherence only between helper photon
numbers zero and two and may use the model's unpriced phase reference.

The input has mean occupation $`3/2`$. The separation also holds with an additional
mean budget $`E=3/2`$: for the achievability theorem, replace the input probabilities
by $`(0,1/2+\epsilon,1/2-\epsilon)`$ with sufficiently small positive $`\epsilon`$.
This supplies energy slack and preserves the strict lower bound by finite-dimensional
entropy continuity. The counting bound already optimizes the larger cutoff simplex.

## The counting bound includes all inputs and codes

The [exact counting reduction](capacity_reduction.md#exact-counting-reduction)
applies to the restricted input space. Joint degradation makes the counting channel
degradable, including the copy of its record in the complement. Coherent information
is concave in the input and additive for this channel. Phase covariance permits
number twirling without decreasing it. Therefore

```math
Q_{\rm cnt}^{[2]}=\max_{p\in\Delta_2}C(p),
\qquad
C(p)=H(J,K)-H(W,K),
```

where $`J,W,K`$ are receiver, inaccessible and helper counts and $`\Delta_2`$ is the
probability simplex on $`n=0,1,2`$. The optimization includes arbitrary input
coherence before twirling and arbitrary correlated endpoint codes before the
degradable-channel reduction. Processing the entire count vector does not improve
the channel.

For $`j+k\le n`$, define

```math
T^B_{jk|n}=\frac{n!}{j!k!(n-j-k)!}a^jc^kb^{n-j-k},
\qquad
q^B_{jk}(p)=\sum_{n=0}^2p_nT^B_{jk|n}.
```

Set the coefficient to zero otherwise. The corresponding $`T^Z_{wk|n}`$ and
$`q^Z_{wk}`$ interchange $`a`$ and $`b`$. At the interior rational point

```math
r=\frac1{100000}(21873,42224,35903),
```

all physically possible joint probabilities are positive. Differentiation gives

```math
g_n=\frac{\partial C}{\partial p_n}(r)
=-\sum_{j,k}T^B_{jk|n}\log_2q^B_{jk}(r)
+\sum_{w,k}T^Z_{wk|n}\log_2q^Z_{wk}(r).
```

The constant derivative terms cancel because each transition column sums to one.
Concavity supplies a global supporting hyperplane. Moreover, the homogeneous
extension satisfies $`C(tp)=tC(p)`$: the two entropy normalization terms cancel.
Thus $`C(r)=\sum_nr_ng_n`$ and

```math
C(p)\le C(r)+g\cdot(p-r)=g\cdot p\le\max_ng_n.
```

Exact rational logarithm enclosures certify $`\max_ng_n<0.318`$. For orientation,
the three components are approximately $`0.3175298364`$, $`0.3175316976`$ and
$`0.3175290546`$. These decimals and a numerical optimizer are not premises of the
upper bound. The bound holds over the entire simplex, including its boundary.

## The coherent detector's attainable rate

For a diagonal input $`p=(p_0,p_1,p_2)`$, the two signs produce unnormalized receiver
states with identical spectra,

```math
B_\pm=\frac12
\begin{pmatrix}
p_0+p_1b+p_2(b^2+c^2)&0&\pm p_2ac\\
0&p_1a+2p_2ab&0\\
\pm p_2ac&0&p_2a^2
\end{pmatrix}.
```

The inaccessible states $`Z_\pm`$ interchange $`a`$ and $`b`$. For the outcome
$`|1\rangle`$, the two unnormalized states are

```math
B_1=\mathrm{diag}(p_1c+2p_2bc,\,2p_2ac,\,0),
\qquad
Z_1=\mathrm{diag}(p_1c+2p_2ac,\,2p_2bc,\,0).
```

These matrices follow directly by contracting the splitter isometry with the three
measurement rows. Define $`s(X)=-\mathrm{Tr}\,X\log_2X`$ for a subnormalized
positive matrix. Each outcome has matching receiver and inaccessible trace, so
the record entropy cancels and the coherent information is

```math
I_c=2[s(B_+)-s(Z_+)]+s(B_1)-s(Z_1).
```

This expression retains the copied classical outcome in the complement. Ordinary
coding for the resulting finite-dimensional flagged channel attains every rate
strictly below $`I_c`$. No optimum over other coherent detectors is asserted.

Each matrix has one scalar eigenvalue and a two-by-two block. If that block has
diagonal entries $`d_0,d_2`$ and off-diagonal entry $`u`$, its eigenvalues are

```math
\lambda_\pm=\frac{d_0+d_2\pm
\sqrt{(d_0-d_2)^2+4|u|^2}}2.
```

At $`p=(0,1/2,1/2)`$, all radicands and scalar entries are rational. Rational
square-root and logarithm enclosures give $`I_c>0.329`$; its diagnostic decimal is
$`0.3295628527472316`$. Together with the supporting-hyperplane bound this proves
the displayed strict separation.

## What must change in the measurement

The [number-diagonal simulation argument](counting_bounds.md#every-number-diagonal-record-is-simulated-by-counting)
shows that diagonal single-mode or joint block effects are classical
postprocessing of full counting, including reference correlations. Such effects
cannot improve the rate. The witness changes the effective measurement by
retaining coherence between helper photon numbers zero and two. This necessity
does not say that an arbitrary coherent POVM improves capacity. It concerns the
effective block effects: diagonal intermediate measurements followed by other
coherent controls need not remain in the diagonal class.

## Relation to the qubit theorem and verification

At photon cutoff $`M=1`$, the [all-input, all-POVM qubit theorem](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/main/research/EXACT_PRODUCT_CAPACITY_2026-10-07.md)
makes counting optimal for these parameters. Cutoff zero has no communication
capacity. The example above therefore locates the first possible **photon-number
cutoff** at $`M=2`$. This is not a minimal input-subspace-dimension theorem: the
witness itself is supported on $`|1\rangle,|2\rangle`$, while its splitter outputs
occupy vacuum through two photons.

The optical [constant-gap theorem](coherent_measurements.md) and counting half-log
law address the distinct mean-energy-only model on the full Fock space. This finite
example neither computes the optimal coherent detector nor bounds unrestricted
optical counting at mean energy $`3/2`$.

Run the [exact arithmetic certificate](../verification/qutrit_certificate.py):

```bash
python verification/qutrit_certificate.py
```

It uses rational range reduction and the series

```math
\ln x=2\sum_{k=0}^{N-1}\frac{t^{2k+1}}{2k+1}+R_N,
\qquad
t=\frac{x-1}{x+1},
\qquad
|R_N|\le\frac{2|t|^{2N+1}}{(2N+1)(1-t^2)}.
```

Range reduction gives $`1\le x\le2`$ and $`0\le t\le1/3`$; sixty terms suffice.
Integer square roots enclose each algebraic eigenvalue radicand with rational
endpoints. Interval arithmetic then certifies both strict rate inequalities.
The script prints diagnostics without changing existing reference outputs. The
written channel reduction and concavity argument establish the arbitrary-input
and arbitrary-code claims; arithmetic certifies their finite evaluation.
