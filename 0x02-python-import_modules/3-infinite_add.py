#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num_args = len(sys.argv) - 1
    res = 0

    for j in range(num_args):
        res += int(sys.argv[j + 1])
    print("{}".format(res))
