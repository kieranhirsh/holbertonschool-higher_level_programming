#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ii in range(len(matrix)):
        ending = " "
        for jj in range(len(matrix[ii])):
            if jj == len(matrix[ii]) - 1 and ii != len(matrix) - 1:
                ending = "\n"
            elif jj == len(matrix[ii]) - 1 and ii == len(matrix) - 1:
                ending = ""

            print("{:d}".format(matrix[ii][jj]), end=ending)
    print("")
