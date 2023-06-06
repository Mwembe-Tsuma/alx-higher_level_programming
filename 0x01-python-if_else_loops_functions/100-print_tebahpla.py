#!/usr/bin/python3

for letter in range(122, 64, -1):
    print(chr(letter), end='') if letter % 2 == 0 else print(chr(letter).upper(), end='')
