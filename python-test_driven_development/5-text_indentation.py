#!/usr/bin/python3
"""
Module contenant une fonction affichant un texte aere
"""


def text_indentation(text):
    """
    Fonction text_indentation qui retourne a la ligne à chaque '.', '?' et ':'

    Parametres :
        - text : string

    Return :
        Un texte qui est separe a chaque signe de ponctuation par un saut de
        lignes.

    Raise :
        - TypeError si text n'est pas un string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    a_afficher = ""
    for i in text:
        a_afficher += i
        if i == "." or i == "?" or i == ":":
            print(a_afficher.strip())
            print("")
            a_afficher = ""
    print(a_afficher, end="")


# text_indentation("Bonjour. Arrive-t-on ? bientot")
