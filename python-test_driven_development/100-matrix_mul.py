#!/usr/bin/python3
''' matrix_mul module '''


def matrix_mul(m_a, m_b):
    ''' this function multiplies two matrices together

    Args:
        m_a (list of list of ints/floats): a matrix
        m_b (list of list of ints/floats): b matrix

    Returns:
        (list of list of ints/floats): a new matrix, equal to m_a * m_b
    '''
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    new_matrix = []
    for ii in range(len(m_a)):
        new_matrix.append([])
        for jj in range(len(m_b[0])):
            new_matrix[ii].append(0)
            for kk in range(len(m_a[0])):
                if (not isinstance(m_a[ii][kk], int) and
                        not isinstance(m_a[ii][kk], float)):
                    raise TypeError("m_a should contain only integers or "
                                    "floats")
                if (not isinstance(m_b[kk][jj], int) and
                        not isinstance(m_b[kk][jj], float)):
                    raise TypeError("m_b should contain only integers or "
                                    "floats")

                new_matrix[ii][jj] += m_a[ii][kk] * m_b[kk][jj]

    return new_matrix
