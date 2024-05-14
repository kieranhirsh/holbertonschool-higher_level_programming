#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda vect: [n ** 2 for n in vect], matrix))
