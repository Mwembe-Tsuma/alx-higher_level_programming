#!/usr/bin/python3
""" Define a func to check instance"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class/subclass.

    Args:
        obj (any): The object
        a_class (type): The calss
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
