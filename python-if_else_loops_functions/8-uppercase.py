#!/usr/bin/python3
def uppercase(str):
    renv = ""
    for car in range(len(str)):
	if ord('a') <= ord(str[car]) <= ord('z'):
	    att = ord(str[car]) - 32
	    renv += chr(att)
	else:
	    renv += str[car]
    print(renv)
