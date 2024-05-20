#!/usr/bin/python3
''' matrix_divided module '''


def matrix_divided(matrix, div):
    ''' this function divides all elements of a matrix by a number

    Args:
        matrix (list of int/float): a matrix
        b (int/float): a divisor

    Returns:
        (list of int/float): the matrix divide by the divisor
    '''
    new_matrix = []
    matrix_length = len(matrix[0])
    for ii in range(len(matrix)):
        if matrix_length != len(matrix[ii]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for jj in range(len(matrix[ii])):
            new_matrix[ii].append(round(matrix[ii][jj] / div,2))

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return new_matrix
