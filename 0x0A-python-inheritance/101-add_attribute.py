#!/usr/bin/python3
"""Define a function to add attribute to an object"""


def add_attribute(obj, att_name, att_value):
    """ Add attribute to an object.

    Args:
        att_name (str): The attribute name
        att_value (any): The attribute value

    Raises:
        TypeError: If can't add new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, att_value)
