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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
