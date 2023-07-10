#!/usr/bin/python3
"""Define Class Myint"""


class MyInt(int):
    """MyInt class representation"""

    def __eq__(self, value):
        """Change the equal(==) operatr"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Change the not equal(!=) operator"""
        return super().__eq__(value)
