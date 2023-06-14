#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_val = 0

    for num in range(len(roman_string) -1, -1, -1):
        curr_val = roman_val.get(roman_string[num], 0)

        if curr_val >= prev_val:
            res += curr_val
        else:
            res -= curr_val

        prev_val = curr_val
    return (res)
