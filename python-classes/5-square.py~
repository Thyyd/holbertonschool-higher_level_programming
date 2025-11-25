#!/usr/bin/python3

""" Module contenant la classe Square """


class Square:
    """Classe qui definit un carre. Definition d'un attribut prive
    size et verifie que size soit un entier positif (Ajout v.0.2).
    Ajout d'une methode renvoyant l'aire du carre (Ajout v.0.3).
    Ajout d'un getter et d'un setter a l'attribut size (Ajout v.0.4)."""
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")

        except (TypeError, ValueError) as e:
            raise e

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

        except (TypeError, ValueError) as e:
            raise e

        self.__size = value

    def area(self):
        return self.__size*self.__size
