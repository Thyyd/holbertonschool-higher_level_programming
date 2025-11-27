#!/usr/bin/python3
"""
Module contenant une fonction affichant deux chaines de caractere,
"""


def say_my_name(first_name, last_name=""):
    """
    Fonction say_my_name affiche les chaines de caractere first_name
    et last_name.

    Parametres :
        - first_name : string
        - last_name : string

    Return :
        Chaine de caractere : "My name is <first_name> <last_name>"

    Raise :
        - TypeError si first_name n'est pas un string
        - TypeError si last_name n'est pas un string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    phrase = "My name is {} {}".format(first_name, last_name)
    return phrase
