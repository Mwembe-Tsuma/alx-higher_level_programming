#!/usr/bin/python3
"""Define a func that append to of a text file"""


def write_file(filename="", text=""):
    """Function that append to a text file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
