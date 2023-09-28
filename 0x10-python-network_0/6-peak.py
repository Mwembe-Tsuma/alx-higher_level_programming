#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find the peak in a list of Int"""

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    idx = int(len(list_of_integers) / 2)

    if idx != len(list_of_integers) - 1:
        if list_of_integers[idx - 1] < list_of_integers[idx] and\
           list_of_integers[idx + 1] < list_of_integers[idx]:
            return list_of_integers[idx]
    else:
        if list_of_integers[idx - 1] < list_of_integers[idx]:
            return list_of_integers[idx]
        else:
            return list_of_integers[idx - 1]

    if list_of_integers[idx - 1] > list_of_integers[idx]:
        peak_list = list_of_integers[0:idx]
    else:
        peak_list = list_of_integers[idx + 1:]

    return find_peak(peak_list)
