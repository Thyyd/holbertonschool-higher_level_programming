#!/usr/bin/python3
"""
Module contenant une fonction divisant par 3 tous
les nombres contenus dans une matrice
"""


def matrix_divided(matrix, div):
    """
    Fonction matrix_divided qui divise tous les nombres presents dans
    une matrice.

    Parametres :
        - matrix : matrice (tableau de tableau) qui contient seulement des
        int ou des float
        - div : int > 0 qui va diviser tous les nombres de matrix

    Return :
        matrix divise par div, avec 2 chiffres decimaux max

    Raise :
        - TypeError si matrix ne contient pas que des int ou des float
        - TypeError si les lignes de matrix ne contiennent pas le meme
        nombre de colonnes
        - TypeError si div n'est pas un nombre
        - ZeroDivisionError si div == 0
    """

    # On verifie que la matrice contient au moins une valeur a diviser.
    if matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Puis on verifie que la matrice est une liste.
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Si matrix est une liste simple qui ne contient que des int/float,
    # alors il faut la transformer en liste de liste : [1, 2] -> [[1, 2]]
    was_list = False
    is_list = True
    for elem in matrix:  # On parcourt les elements de matrix
        if not isinstance(elem, (int, float)):
            is_list = False
            break
            # Si elem n'est pas un chiffre, ce n'est pas une liste simple.

    # Transformation liste simple en liste de liste
    if is_list:
        matrix = [matrix]
        was_list = True

    # On verifie ensuite que chaque element de matrix est une liste
    for row in matrix:  # row est une liste de matrix
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        # On verifie enfin que la valeur dans la liste de liste
        # est bien un nombre.
        for val in row:  # val est la valeur contenue dans row
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    " integers/floats")

    list_size = len(matrix[0])  # Variable contenant la taille de la ligne 0
    # Verification que toutes les lignes de matrix font la meme taille
    for i in range(len(matrix)):
        if len(matrix[i]) != list_size:
            raise TypeError("Each row of the matrix must have the same size"
                            )

    # Verification div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Verification div est un nombre > 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mat2 = []  # Nouvelle matrice divisee
    # Boucle ajoutant les valeurs modifiees dans la nouvelle matrixe.
    for r in matrix:
        line = []
        for x in r:
            line.append(round(x / div, 2))
        mat2.append(line)

    # Si la matrice initiale etait de dimension 1, on retourne une simple liste
    if was_list:
        mat2 = mat2[0]

    return mat2
