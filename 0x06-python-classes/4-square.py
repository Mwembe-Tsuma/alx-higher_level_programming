#!/usr/bin/python3
"""Defination a class Square."""


class Square:
    """Representation of a square."""
    def __init__(self, size=0):
        """Initialize an instance of a square.
        Args:
            size(int)
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size_setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to return the current area of the square."""
        return (self.__size * self.__size)
