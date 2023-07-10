#!/usr/bin/python3
"""Define class Mylist that inherits list"""


class Mylist(list):
    """Implement sorted print for the built in list class."""
    def print_sorted(self):
        """Prints list in ascending sort."""
        print(sorted(self))
