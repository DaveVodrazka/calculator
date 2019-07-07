from _type_check import int_or_float_check, int_check
from greatest_common_divisor import GCD
from abs import abs
from multiply import multiply
from divide import divide
from add import add
from modulo import modulo


def power(a, b):
    int_or_float_check(a)
    int_or_float_check(b)
    if isinstance(b, float):
        frac = get_fraction(b)
        if frac[0] < 0:
            return int_root(divide(1, int_power(a, abs(frac[0]))), frac[1])
        else:
            return int_root(int_power(a, frac[0]), frac[1])
    elif b >= 0:
        return int_power(a, b)
    else:
        return divide(1, int_power(a, abs(b)))


def get_fraction(a):
    # Turns float into fraction
    int_or_float_check(a)
    if isinstance(a, int):
        return a, 1
    else:
        is_negative = False
        if a < 0:
            is_negative = True
            a = abs(a)
        fraction = str(a).split(".")
        original_denominator = 1
        for i in range(len(fraction[1])):
            original_denominator = multiply(original_denominator, 10)
        original_numerator = int(fraction[0] + fraction[1])  # Not addition but string concat
        common_denominator = GCD(original_numerator, original_denominator)
        numerator = int(divide(original_numerator, common_denominator))
        denominator = int(divide(original_denominator, common_denominator))
    if is_negative:
        return -numerator, denominator
    else:
        return numerator, denominator


def int_power(a, b):
    # Raises a to the power b, where b needs to be an int
    int_or_float_check(a)
    int_check(b)
    res = 1
    for i in range(b):
        res = multiply(res, a)
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
