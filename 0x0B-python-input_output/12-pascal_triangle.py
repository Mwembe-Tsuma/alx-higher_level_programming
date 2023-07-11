#!/usr/bin/python3
"""Define a pascal triangle function"""


def pascal_triangle(n):
    """Rep of a pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        new_triangle = triangle[-1]
        temp = [1]
        for idx in range(len(new_triangle) - 1):
            temp.append(new_triangle[idx] + new_triangle[idx + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
