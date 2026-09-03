#Unit tests for zad2.py
import unittest
from zad2 import CiagGeometryczny
class TestCiagGeometryczny(unittest.TestCase):
    def test_ilorazRownyJeden(self):
        ciag = CiagGeometryczny(2, 2)
        self.assertEqual(ciag.kolejne_wyrazy(3), [2, 4, 8])
    def test_ilorazUlamek(self):
        ciag = CiagGeometryczny(8, 0.5)
        self.assertEqual(ciag.kolejne_wyrazy(3), [8, 4, 2])
    def test_ilorazUjemny(self):
        ciag = CiagGeometryczny(2, -2)
        self.assertEqual(ciag.kolejne_wyrazy(3), [2, -4, 8])
    def test_ilorazJeden(self):
        ciag = CiagGeometryczny(2, 1)
        self.assertEqual(ciag.kolejne_wyrazy(3), [2, 2, 2])
    def test_ilorazZero(self):
        ciag = CiagGeometryczny(1, 0)
        self.assertEqual(ciag.kolejne_wyrazy(3), [1, 0, 0])
    def test_jedenWyraz(self):
        ciag = CiagGeometryczny(2, 3)
        self.assertEqual(ciag.kolejne_wyrazy(1), [2])
    def test_poprawnaLiczbaWyrazow(self):
        ciag = CiagGeometryczny(2, 3)
        self.assertEqual(len(ciag.kolejne_wyrazy(5)), 5)