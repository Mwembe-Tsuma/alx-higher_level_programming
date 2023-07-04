#!/usr/bin/python3
"""Defines a matrix mul function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats)
        m_b (list of lists of ints/floats)
    Raises:
        TypeError: If m_a or m_b is not a list of lists of int or float.
        TypeError: If m_a or m_b is empty.
        TypeError: If m_a or m_b are different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [x for row in m_a for x in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [x for row in m_b for x in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_matrix = []
    for rows in range(len(m_b[0])):
        new_rows = []
        for cols in range(len(m_b)):
            new_rows.append(m_b[cols][rows])
        inverted_matrix.append(new_rows)

    matrixA = []
    for row in m_a:
        new_rows = []
        for col in inverted_matrix:
            res = 0
            for y in range(len(inverted_matrix[0])):
                res += row[y] * col[y]
            new_rows.append(res)
        matrixA.append(new_rows)

    return matrixA
