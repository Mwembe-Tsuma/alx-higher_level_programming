#!/usr/bin/python3
"""Defination a class Square."""


class Square:
    """Representation of a square."""
    def __init__(self, size=0):
        """Initialize an instance of a square.
        Args:
            size(int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Method to return the area of the square."""
        return (self.__size * self.__size)
