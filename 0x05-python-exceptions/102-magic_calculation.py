#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            else:
                res += a ** b / n
        except:
            res = b + a
            break
    return (res)
