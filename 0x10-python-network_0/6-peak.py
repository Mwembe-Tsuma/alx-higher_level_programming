#!/usr/bin/python3


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    for idx in range(1, len(list_of_integers) - 1):
        if list_of_integers[idx] >= list_of_integers[idx - 1] and\
              list_of_integers[idx] >= list_of_integers[idx + 1]:
            return list_of_integers[idx]

    return None
