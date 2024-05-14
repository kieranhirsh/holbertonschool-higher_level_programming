#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda vect: list(map(lambda n: n ** 2, vect)), matrix))
