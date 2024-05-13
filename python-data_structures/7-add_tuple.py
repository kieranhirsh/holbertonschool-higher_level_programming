#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        temple_a = list(tuple_a)
        for ii in range(len(tuple_a), 2):
            temple_a.append(0)
            tuple_a = tuple(temple_a)

    if len(tuple_b) < 2:
        temple_b = list(tuple_b)
        for ii in range(len(tuple_b), 2):
            temple_b.append(0)
            tuple_b = tuple(temple_b)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
