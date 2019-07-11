from _type_check import int_or_float_check
from abs import abs
from divide import divide
from multiply import multiply
from greatest_common_divisor import GCD


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
        numerator = -numerator
    return numerator, denominator
