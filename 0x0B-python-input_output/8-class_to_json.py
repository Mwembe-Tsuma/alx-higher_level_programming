#!/usr/bin/python3
"""Defination of a class to JSON function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
