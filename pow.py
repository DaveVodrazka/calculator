import sys
from _type_check import int_or_float_check, int_check
from greatest_common_divisor import GCD
from abs import abs
from multiply import multiply
from divide import divide
from add import add
from modulo import modulo
from fraction import get_fraction


def power(a, b):
    int_or_float_check(a)
    int_or_float_check(b)
    if isinstance(b, int):
        if b == 0:
            return 1
        elif b > 0:
            return int_power(a, b)
        elif b < 0:
            return divide(1, int_power(a, abs(b)))

    frac = get_fraction(b)
    if frac[0] > 0:
        first_step = int_power(a, frac[0])
        result = int_root(first_step, frac[1])
        return result
    elif frac[0] < 0:
        first_step = divide(1, int_power(a, abs(frac[0])))
        result = int_root(first_step, frac[1])
        return result


def int_power(a, b):
    # Raises a to the power b, where b needs to be an int
    int_or_float_check(a)
    int_check(b)
    res = 1
    for i in range(b):
        res = multiply(res, a)
    if res == 0 and a > 0:
        return sys.float_info.min
    else:
        return res


def int_root(a, n):
    # Return n-th root of a, where b needs to be an int
    int_or_float_check(a)
    int_check(n)
    if n == 0:
        raise SyntaxError("Cannot calculate zero-th root")
    if a < 0 and modulo(n, 2) == 0:
        raise SyntaxError("Cannot do even root of negative number")
    epsilon = .00001
    x_0 = divide(a, n)
    x_1 = multiply(divide(1, n), add(multiply(add(n, -1), x_0), divide(a, int_power(x_0, add(n, -1)))))
    while abs(add(x_0, -x_1)) > epsilon:
        x_0 = x_1
        x_1 = multiply(divide(1, n), add(multiply(add(n, -1), x_0), divide(a, int_power(x_0, add(n, -1)))))
    return x_1
