#!/usr/bin/python3
"""Defines class Mylist that inherits list."""


class MyList(list):
    """Implements sorted printing for list class."""

    def print_sorted(self):
        """Print a list in sorted order."""
        print(sorted(self))
