#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = matrix.copy()

    for idx in range(len(matrix)):
        res[idx] = list(map(lambda x: x**2, matrix[idx]))
    return(res)
