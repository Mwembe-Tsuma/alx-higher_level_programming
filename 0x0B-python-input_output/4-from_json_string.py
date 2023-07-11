#!/usr/bin/python3
"""Define a function that returns the object represented by python str"""
import json


def from_json_string(my_str):
    """returns the object represented by python str"""
    return json.loads(my_str)
