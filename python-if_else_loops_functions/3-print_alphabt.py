#!/usr/bin/python3
for lettre in range(ord('a'), ord('z') + 1):
    if chr(lettre) != 'e' and chr(lettre) != 'q':
        print("{}".format(chr(lettre)), end="")
