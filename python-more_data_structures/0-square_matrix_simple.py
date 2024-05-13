#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [None] * len(matrix)
    for ii in range(len(new_matrix)):
        new_matrix[ii] = [None] * len(matrix[ii])
        for jj in range(len(new_matrix[ii])):
            new_matrix[ii][jj] = matrix[ii][jj] ** 2

    return new_matrix
