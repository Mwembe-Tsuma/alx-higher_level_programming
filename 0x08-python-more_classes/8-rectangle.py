#!/usr/bin/python3
"""Define a Rectangle Class."""


class Rectangle:
    """Rep a Rectangle.

    Attributes:
        number_of_instances (int):The number of Rect instances.
        print_symbol (any): The symbol used for string rep."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Find the area of the Rect."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Find the perimeter of the Rect."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * ((self.__width) + (self.__height)))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): 1st instance of Rectangle.
            rect_2 (Rectangle): 2nd instance of Rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for idx in range(self.__height):
            [rect.append(str(self.print_symbol)) for i in range(self.__width)]
            if idx != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Bye my Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
