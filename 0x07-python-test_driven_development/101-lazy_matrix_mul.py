#!/usr/bin/python3
"""Defines a matrix multiplication fun using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the mul results of 2 matrices.

    Args:
        m_a (list of lists of ints/floats)
        m_b (list of lists of ints/floats)
    """

    return (np.matmul(m_a, m_b))
