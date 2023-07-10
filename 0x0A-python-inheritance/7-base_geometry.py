#!/usr/bin/python3
"""Define class BaseGeometry."""


class BaseGeometry:
    """Representation of class BaseGeometry."""
    def area(self):
        """Instance method to raise execption area() is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value.
        
        Args:
            name (string): The name
            value (int): The value

        Riases:
            TypeError: If value is not an int
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
