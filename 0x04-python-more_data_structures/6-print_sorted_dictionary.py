#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    for num in my_keys:
        print("{}: {}".format(num, a_dictionary.get(num)))
