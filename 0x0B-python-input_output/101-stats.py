#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


def print_stats(size, code_status):
    """Print  metrics.

    Args:
        size (int): The accumulated file size.
        code_status (dict): The accumulated count.
    """
    print("File size: {}".format(size))
    for k in sorted(code_status):
        print("{}: {}".format(k, code_status[k]))


if __name__ == "__main__":
    import sys

    size = 0
    code_status = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for line in sys.stdin:
            if counter == 10:
                print_stats(size, code_status)
                counter = 1
            else:
                counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if code_status.get(line[-2], -1) == -1:
                        code_status[line[-2]] = 1
                    else:
                        code_status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, code_status)

    except KeyboardInterrupt:
        print_stats(size, code_status)
        raise
