def int_or_float_check(a):
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("Required int or float and got: ", a)


def int_check(a):
    if not isinstance(a, int):
        raise TypeError("Required int and got: ", a)
