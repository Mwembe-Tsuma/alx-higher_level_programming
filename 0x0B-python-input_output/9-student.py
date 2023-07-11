#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Rep a Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """ Dict representation of a student"""
        return self.__dict__
