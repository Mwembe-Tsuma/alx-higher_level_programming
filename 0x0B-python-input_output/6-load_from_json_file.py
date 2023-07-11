#!/usr/bin/python3
"""Define a function that create an object from JSON file"""
import json


def load_from_json_file(filename):
    """returns the object created from JSON file"""
    with open(filename, "r") as fd:
        return json.loads(fd.read())
