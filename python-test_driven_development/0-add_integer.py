#!/usr/bin/python3
"""
Module contenant une fonction ajoutant deux nombres.
"""

def add_integer(a, b=98):
    """
    Fonction add_integer qui ajoute les deux nombres entres en parametres.

    Parametres :
	a : premier terme a ajouter (int ou float)
        b : deuxieme terme a ajouter (int ou float, valeur par defaut 98)

    Return :
       	Somme entiere de a et b

    Raise :
        TypeError si a ou b n'est pas un int ou un float
    """

    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

    except (TypeError) as e:
        raise e

    return int(a) + int(b)
