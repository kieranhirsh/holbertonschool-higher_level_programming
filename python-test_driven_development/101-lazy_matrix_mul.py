#!/usr/bin/python3
''' lazy_matrix_mul module '''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    ''' this function multiplies two matrices together

    Args:
        m_a (list of list of ints/floats): a matrix
        m_b (list of list of ints/floats): b matrix

    Returns:
        (list of list of ints/floats): a new matrix, equal to m_a * m_b
    '''
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("setting an array element with a sequence.")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("setting an array element with a sequence.")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: {} (dim 1) "
                         "!= {} (dim 0)".format(len(m_a), len(m_a[0]),
                                                len(m_b), len(m_b[0]),
                                                len(m_a[0]), len(m_b)))
    for ii in range(len(m_a)):
        for jj in range(len(m_a[0])):
            if (not isinstance(m_a[ii][jj], int) and
                    not isinstance(m_a[ii][jj], float)):
                raise TypeError("invalid data type for einsum")
    for ii in range(len(m_b)):
        for jj in range(len(m_b[0])):
            if (not isinstance(m_b[ii][jj], int) and
                    not isinstance(m_b[ii][jj], float)):
                raise TypeError("invalid data type for einsum")

    new_matrix = np.matmul(m_a, m_b)

    return new_matrix
