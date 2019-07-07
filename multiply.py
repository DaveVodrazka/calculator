from _type_check import int_or_float_check


def multiply(a, b):
    # Multiplication operation
    int_or_float_check(a)
    int_or_float_check(b)
    return a * b
