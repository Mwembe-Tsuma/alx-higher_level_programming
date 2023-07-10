#!/usr/bin/python3
"""Define class Rectangle that inherit BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of class Rectangle that inherit BaseGeometry."""
    def __init__(self, width, height):
        """Initialize new rectangle

        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
