from _type_check import int_check
from add import add


def modulo(a, b):
    # Return the remainder of whole division
    int_check(a)
    int_check(b)
    while a >= b:
        a = add(a, -b)
    return a
