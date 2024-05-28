#!/usr/bin/python3
''' module documentation '''


def pascal_triangle(n):
    '''
    this function returns Pascals triangle

    Arguments:
        n (int): the desired Pascal's triangle size

    Returns:
        triangle (list of lists of int): Pascal's triangle of size n
    '''
    triangle = []

    for ii in range(n):
        triangle.append([None] * (ii + 1))
        triangle[ii][0] = 1
        triangle[ii][-1] = 1
        for jj in range(1, ii):
            triangle[ii][jj] = triangle[ii - 1][jj - 1] + triangle[ii - 1][jj]

    return triangle
