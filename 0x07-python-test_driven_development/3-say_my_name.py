#!/usr/bin/python3

# 3-say_my_name.py
"""Defines a name printing fun."""


def say_my_name(first_name, last_name=""):
    """Print a first and last name.

    Args:
        first_name (str)
        last_name (str)
    Raises:
        TypeError: If first_name or last_name is not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
