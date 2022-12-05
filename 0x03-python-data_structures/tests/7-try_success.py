#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if (length_a > 1) and (length_b > 1):
        return (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])

    elif (length_a > 1) and (length_b == 1):
        return (tuple_a[0]+tuple_b[0], tuple_a[0])

    elif (length_a > 1) and (length_b == 0):
        return (tuple_a)

    elif (length_a == 1) and (length_b > 1):
        return (tuple_a[0]+tuple_b[0], tuple_b[1])

    elif (length_a == 1) and (length_b == 1):
        return (tuple_a[0]+tuple_b[0], 0)

    elif (length_a == 1) and (length_b == 0):
        return (tuple_a[0], 0)

    elif (length_a == 0) and (length_b > 1):
        return (tuple_b)

    elif (length_a == 0) and (length_b == 1):
        return (tuple_b[0], 0)

    elif (length_a == 0) and (length_b == 0):
        return (0, 0)

    else:
        y = 0
