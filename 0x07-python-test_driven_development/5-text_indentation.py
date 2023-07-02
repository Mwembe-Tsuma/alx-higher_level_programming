#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentation fun."""


def text_indentation(text):
    """Print two new lines after each '.', '?', and ':' chars.

    Args:
        text (string)
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    res = 0
    while res < len(text) and text[res] == ' ':
        res += 1

    while res < len(text):
        print(text[res], end="")
        if text[res] == "\n" or text[res] in ".?:":
            if text[res] in ".?:":
                print("\n")
            res += 1
            while res < len(text) and text[res] == ' ':
                res += 1
            continue
        res += 1
