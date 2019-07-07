from _type_check import int_or_float_check


def divide(a, b):
    # Multiplication operation
    int_or_float_check(a)
    int_or_float_check(b)
    if b == 0:
        raise SyntaxError("Cannot divide by 0")
    return a / b
