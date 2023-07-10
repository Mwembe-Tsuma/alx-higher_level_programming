#!/usr/bin/python3
"""Define a lookup function"""


def lookup(obj):
    """Func to returns the list of available attributes
    and methods of an object:
    """
    return (dir(obj))
