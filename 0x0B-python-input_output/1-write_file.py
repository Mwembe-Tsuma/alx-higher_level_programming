#!/usr/bin/python3
"""Define a func that writes to of a text file"""


def write_file(filename="", text=""):
    """Function that writes to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
