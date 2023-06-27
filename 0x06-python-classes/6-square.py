#!/usr/bin/python3

"""Defination a class Square."""


class Square:
    """Representation of a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize an instance of a square.
        Args:
            size(int)
            position(int, int)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method to return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square wtih # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for j in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for m in range(self.__size)]
            print("")
