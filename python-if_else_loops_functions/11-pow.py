#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        if b < 0:
            res /= a
        else:
            res *= a

    return res
