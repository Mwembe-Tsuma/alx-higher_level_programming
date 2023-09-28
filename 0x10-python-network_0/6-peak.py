#!/usr/bin/python3


def find_peak(list_of_integers):

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
