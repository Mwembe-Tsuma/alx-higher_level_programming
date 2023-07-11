#!/usr/bin/python3
"""Define a func that reads contents of a file"""


def read_file(filename=""):
    """Function to read a file."""
    with open(filename, encoding="utf-8") as file:
        fd = file.read()
        print(fd)
