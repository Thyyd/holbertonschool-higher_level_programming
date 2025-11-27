#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
Module Test de la fonction max_integer
"""


class TestMaxInteger(unittest.TestCase):
    """
    Classe contenant plusieurs fonctions de test, permettant de vérifier :
    - Les Valeurs
    - Les Types
    - La valeur renvoyee par la fonction
    """

    def test_type(self):
        # Etre sur que les TypeError sont relevées quand necessaire
        self.assertRaises(TypeError, max_integer, ["a", 50])
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 92)
        self.assertRaises(TypeError, max_integer, (32, 85, 120))

    def test_maxint(self):
        # Etre sur que la Fonction renvoie la bonne valeur
        # First, With only positive int values
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([25]), 25)
        self.assertEqual(max_integer([10, 10, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([15, 20, 75, 10]), 75)
        self.assertEqual(max_integer([750, 12, 96, 34]), 750)
        # Then, with positive float values
        self.assertAlmostEqual(max_integer([12.5, 13.0, 8.2]), 13.0)
        # Then, with mixed positive float and int values
        self.assertAlmostEqual(max_integer([5, 12.5, 7.5, 14, 17.5]), 17.5)
        # Then, with negative values
        self.assertEqual(max_integer([-2, -10, -50]), -2)
        # Finally, a mix of all
        self.assertAlmostEqual(max_integer([-2, -3.5, 9.25, 7.3]), 9.25)
