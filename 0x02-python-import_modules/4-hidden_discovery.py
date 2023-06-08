#!/usr/bin/python3

import hidden_4

list_of_names = dir(hidden_4)

for name in list_of_names:
    if name[:2] != "__":
        print(name)
