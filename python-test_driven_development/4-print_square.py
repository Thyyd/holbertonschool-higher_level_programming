#!/usr/bin/python3
"""
Module contenant une fonction affichant un carre avec des #
"""


def print_square(size):
    """
    Fonction print_square affiche un carre de taille size avec des #

    Parametres :
        - size : int

    Return :
        Un carre de taille size avec le caractere #.

    Raise :
        - TypeError si size n'est pas un entier
        - ValueError si size est strictement negatif (size < 0)
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return
    for row in range(size):
        for line in range(size):
            print("#", end="")
            if line == size - 1:
                print("")
