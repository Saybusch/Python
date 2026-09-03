#Unit tests for zad1.py
import unittest
from zad1 import CiagArytmetyczny
class TestCiagArytmetyczny(unittest.TestCase):
    def test_positiveDifference(self):
        ciag = CiagArytmetyczny(2, 3)
        self.assertEqual(ciag.kolejne_wyrazy(2), [2, 5])
    def test_negativeDifferenece(self):
        ciag = CiagArytmetyczny(2, -3)
        self.assertEqual(ciag.kolejne_wyrazy(2), [2, -1])
    def test_zeroDifference(self):
        ciag = CiagArytmetyczny(2, 0)
        self.assertEqual(ciag.kolejne_wyrazy(2), [2, 2])
    def test_oneSign(self):
        ciag = CiagArytmetyczny(2, 3)
        self.assertEqual(ciag.kolejne_wyrazy(1), [2])
    def test_amountOfNumbers(self):
        ciag = CiagArytmetyczny(2, 3)
        self.assertEqual(len(ciag.kolejne_wyrazy(5)), 5)