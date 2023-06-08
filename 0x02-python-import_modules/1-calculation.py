#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    res = add(a, b)
    diff = sub(a, b)
    mul1 = mul(a, b)
    div1 = div(a, b)

    print("{} + {} = {}".format(a, b, res))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, mul1))
    print("{} / {} = {}".format(a, b, div1))
