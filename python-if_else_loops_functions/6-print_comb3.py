#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if (10 * i + j) % 10 > i:
            print("{:02}".format(10*i+j), end=", ")


print("89")
