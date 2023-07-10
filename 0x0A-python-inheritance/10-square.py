#!/usr/bin/python3
"""Define class Square that inherit Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of class Square that inherit Rectangle."""
    def __init__(self, size):
        """Initialize new Square

        Args:
            size (int): Square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, sieze)
        self.__size = size
