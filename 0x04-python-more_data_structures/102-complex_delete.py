#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_to_del = list(a_dictionary.keys())
    for key in key_to_del:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return(a_dictionary)
