#!/usr/bin/python3
"""Define a Rectangle Class."""


class Rectangle:
    """Rep a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set the width of the rect."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and set the height of the rect."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Find the area of rect."""
        return(self.__width * self.__height)

    def perimeter(self):
        """Find the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * ((self.__width ) + (self.__height)))
