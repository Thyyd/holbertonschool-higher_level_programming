#!/usr/bin/python3

""" Module contenant la classe Square """


class Square:
    """Classe qui definit un carre. Definition d'un attribut prive
    size et verifie que size soit un entier positif (Ajout V.0.2)"""
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            
        except (TypeError, ValueError) as e:
            raise e

        self.__size = size
