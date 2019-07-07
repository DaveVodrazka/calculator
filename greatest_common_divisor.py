from modulo import modulo


def GCD(a, b):
    # Return the greatest common divisor
    if a == b:
        return a
    elif a < b:
        c = a
        a = b
        b = c
    while b > 0:
        c = b
        b = modulo(a, b)
        a = c
    return a
