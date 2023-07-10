#!/usr/bin/python3
""" Define a func to check instance"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that
    inherited (directly or indirectly)

    Args:
        obj (any): The object
        a_class (type): The calss
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
