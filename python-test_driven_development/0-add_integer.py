#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float) or a % 0 != 0:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float) or b % 0 != 0:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
