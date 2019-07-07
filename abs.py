from _type_check import int_or_float_check


def abs(a):
    int_or_float_check(a)
    if a < 0:
        return -a
    else:
        return a
