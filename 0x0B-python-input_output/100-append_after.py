#!/usr/bin/python3
"""Define line insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Append a new line after each line containg a given string.

    Args:
        search_string (str): String to search
        new_string (str): new string to append
    """
    txt = ""
    with open(filename) as fd:
        for line in fd:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as f:
        f.write(txt)
