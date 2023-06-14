#!/usr/bin/python3

def number_keys(a_dictionary):
    results = 0
    my_keys = list(a_dictionary.keys())

    for num in my_keys:
        results += 1
    return(results)
