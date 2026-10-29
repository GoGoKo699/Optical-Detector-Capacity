"""Exact rational certificate for the per-mode cutoff-two detector separation.

The channel reduction and branch formulas are proved in
science/qubit_optical_bridge.md. Float values in the JSON are diagnostics only;
all certified comparisons use fractions and remain active under ``python -O``.
"""

from fractions import Fraction as F
from math import factorial, isqrt
import json


LOG_TERMS = 60
SQRT_SCALE = 10**40


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    products = [a * b for a in x for b in y]
    return min(products), max(products)


def scale(x, coefficient):
    return mul(x, (coefficient, coefficient))


def div(x, y):
    require(y[0] > 0, "Interval division requires a positive denominator")
    return mul(x, (1 / y[1], 1 / y[0]))


def ln_unit(x):
    require(1 <= x <= 2, "Logarithm range reduction failed")
    t = (x - 1) / (x + 1)
    partial = 2 * sum(
        (t ** (2 * k + 1) / F(2 * k + 1) for k in range(LOG_TERMS)), F(0)
    )
    remainder = (
        2 * t ** (2 * LOG_TERMS + 1)
        / F(2 * LOG_TERMS + 1) / (1 - t * t)
    )
    return partial, partial + remainder


LN2 = ln_unit(F(2))


def ln(x):
    require(x > 0, "Logarithm requires a positive argument")
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x > 2:
        x /= 2
        exponent += 1
    return add(ln_unit(x), scale(LN2, F(exponent)))


def log2(x):
    return div(ln(x), LN2)


def phi_interval(x):
    lo, hi = x
    require(0 <= lo <= hi, "Entropy received an invalid interval")
    if hi == 0:
        return F(0), F(0)
    require(lo > 0, "Positive entropy atom must be bounded away from zero")
    logarithms = log2(lo)[0], log2(hi)[1]
    return neg(mul(x, logarithms))


def sqrt_interval(x):
    require(x >= 0, "Square root requires a nonnegative argument")
    integer = isqrt(x.numerator * SQRT_SCALE * SQRT_SCALE // x.denominator)
    lo, hi = F(integer, SQRT_SCALE), F(integer + 1, SQRT_SCALE)
    require(lo * lo <= x <= hi * hi, "Square-root enclosure failed")
    return lo, hi


def eig2(d0, d2, off_squared):
    root = sqrt_interval((d0 - d2) ** 2 + 4 * off_squared)
    trace = d0 + d2, d0 + d2
    return scale(sub(trace, root), F(1, 2)), scale(add(trace, root), F(1, 2))


def entropy(values):
    result = F(0), F(0)
    for value in values:
        result = add(result, phi_interval(value))
    return result


def exact(value):
    return value, value


def branch_entries(t, u, c, p):
    """Rational entries for one output; interchange t,u for its complement."""
    return {
        "d0": (p[0] + p[1] * u + p[2] * (u * u + c * c)) / 2,
        "d1": (p[1] * t + 2 * p[2] * t * u) / 2,
        "d2": p[2] * t * t / 2,
        "off_squared": (p[2] * t * c / 2) ** 2,
        "one": (p[1] * c + 2 * p[2] * u * c, 2 * p[2] * t * c),
    }


def conditional_entropy(t, u, c, p):
    entries = branch_entries(t, u, c, p)
    lo, hi = eig2(entries["d0"], entries["d2"], entries["off_squared"])
    signs = entropy([lo, exact(entries["d1"]), hi])
    one = entropy([exact(value) for value in entries["one"]])
    return add(scale(signs, F(2)), one)


def joint_mats(t, u, c):
    rows = []
    for received in range(3):
        for counted in range(3 - received):
            row = []
            for number in range(3):
                lost = number - received - counted
                if lost < 0:
                    row.append(F(0))
                else:
                    coefficient = F(
                        factorial(number),
                        factorial(received) * factorial(counted) * factorial(lost),
                    )
                    row.append(coefficient * t**received * c**counted * u**lost)
            rows.append(row)
    return rows


def grad_component(number, receiver, inaccessible, point):
    result = F(0), F(0)
    for sign, transition in [(-1, receiver), (1, inaccessible)]:
        for row in transition:
            probability = sum((row[j] * point[j] for j in range(3)), F(0))
            if row[number]:
                result = add(result, scale(log2(probability), sign * row[number]))
    return result


def certificate():
    a, b, c = F(1, 5), F(2, 25), F(18, 25)
    p = F(0), F(1, 2), F(1, 2)
    require(a > b > 0 and c > 0 and a + b + c == 1, "Invalid split")
    require(sum(p) == 1 and min(p) >= 0, "Invalid witness input")
    witness = sub(conditional_entropy(a, b, c, p), conditional_entropy(b, a, c, p))

    # Degradability and phase twirling reduce counting to C(p)=H(B,K)-H(Z,K).
    # Its homogeneous concave extension has C(p)<=grad(C)(r).p. The maximum
    # over the entire probability simplex is therefore <=max_n grad_n(C)(r).
    point = F(21873, 100000), F(42224, 100000), F(35903, 100000)
    require(sum(point) == 1 and min(point) > 0, "Invalid interior tangent point")
    receiver, inaccessible = joint_mats(a, b, c), joint_mats(b, a, c)
    for transition in (receiver, inaccessible):
        for number in range(3):
            require(sum(row[number] for row in transition) == 1, "Transition not normalized")
    gradient = [grad_component(n, receiver, inaccessible, point) for n in range(3)]
    upper = max(component[1] for component in gradient)
    require(upper < F(318, 1000), "Counting upper bound not certified")
    require(witness[0] > F(329, 1000), "Witness lower bound not certified")
    require(witness[0] - upper > F(11, 1000), "Strict separation not certified")

    return {
        "claim_scope": "per-mode support |0>,|1>,|2>; arbitrary endpoint codes; no full-Fock comparison",
        "split": ["1/5", "2/25", "18/25"],
        "input": ["0", "1/2", "1/2"],
        "measurement": ["|1>", "(|0>+|2>)/sqrt(2)", "(|0>-|2>)/sqrt(2)"],
        "counting_tangent_point": [str(value) for value in point],
        "counting_gradient_intervals_diagnostic": [[float(x) for x in value] for value in gradient],
        "counting_capacity_strict_upper": "0.318",
        "witness_rate_interval_diagnostic": [float(x) for x in witness],
        "witness_rate_strict_lower": "0.329",
        "separation_strict_lower": "0.011",
        "exact_arithmetic_assertions_passed": True,
    }


def main():
    print(json.dumps(certificate(), indent=2))


if __name__ == "__main__":
    main()
