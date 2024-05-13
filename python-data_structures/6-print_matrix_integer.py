#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ii in range(len(matrix)):
        for jj in range(len(matrix[ii])):
            if jj == len(matrix[ii]) - 1:
                print("{:d}".format(matrix[ii][jj]))
            else:
                print("{:d} ".format(matrix[ii][jj]), end="")
