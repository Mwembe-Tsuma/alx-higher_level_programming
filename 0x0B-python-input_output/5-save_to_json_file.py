#!/usr/bin/python3
"""Define  function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file."""
    with open(filename, "w") as file:
        json.dumb(my_obj, file)
