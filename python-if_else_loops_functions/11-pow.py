#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        res *= a
        if b < 0:
            res = 1 / res

    return res
