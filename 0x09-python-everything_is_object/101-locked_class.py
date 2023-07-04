#!/usr/bin/python3

"""Define a locked class"""


class LockedClass:
    """Representation of a locked class that prevent a user from
    creating a new instance attributes, except first_name.
    """
    __slots__ = ["first_name"]
