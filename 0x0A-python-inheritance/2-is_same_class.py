#!/usr/bin/python3
""" Define a func to check instance"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object
        a_class (type): The calss
    """
    return type(obj) == a_class
