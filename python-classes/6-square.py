#!/usr/bin/python3

""" Module contenant la classe Square """


class Square:
    """Classe qui definit un carre (Ajout v.0). Definition d'un attribut
    prive size (Ajout v.0.1) et verifie que size soit un entier positif
    (Ajout v.0.2).
    Ajout d'une methode renvoyant l'aire du carre (Ajout v.0.3).
    Ajout d'un getter et d'un setter a l'attribut size (Ajout v.0.4).
    Ajout d'une methode affichant le carre utilisant des '#' (Ajout v.0.5)
    Ajout d'un attribut prive position, definit par la methode init ou par
    son setter. Mise a Jour de la methode my_print pour ajouter un decalage
    selon les valeurs contenues dans l'attibut position (Ajout v.0.6)"""
    def __init__(self, size=0, position=(0, 0)):
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")

        except (TypeError, ValueError) as e:
            raise e

        self.__size = size
        try:
            if (type(position) is not tuple
                or len(position) != 2):
                raise TypeError("position must be a tuple of 2 positive integers")

            for x in position:
                if (type(x) is not int
                   or x < 0):
                    raise TypeError("position must be a tuple of 2 positive integers")

        except (TypeError) as e:
            raise e

        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if (type(value) is not tuple
                or len(value) != 2):
                raise TypeError("position must be a tuple of 2 positive integers")

            for x in value:
                if (type(x) is not int
                   or x < 0):
                    raise TypeError("position must be a tuple of 2 positive integers")

        except (TypeError) as e:
            raise e

        self.__position = value

    def area(self):
        return self.__size*self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")

            for l in range(self.__size):
                print("#", end="")
                if l == self.__size - 1:
                    print("")
