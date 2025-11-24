#!/usr/bin/python3

""" Module contenant la classe Square """


class Square:
    """Classe qui definit un carre.
    Definition d'un attribut prive size (Ajout V.0.2)"""
    def __init__(self, size = 0):
        try:
            size = int(size)
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
            
        self.__size = size
