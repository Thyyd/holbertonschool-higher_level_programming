#!/usr/bin/python3
def islower(c):
    retour = None
    if ord('a') <= ord(c) and ord(c) <= ord('z'):
        retour = True
    else:
        retour = False
    
    return retour
