#!/usr/bin/python3
# 0-add_integer.py
"""Defines function to add two int."""


def add_integer(a, b=98):
    """Return sum of a and b.

    Float args are typecasted to int before addition.

    Raises:
        TypeError: If integers are a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
