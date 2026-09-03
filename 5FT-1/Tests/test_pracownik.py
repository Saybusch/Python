#Unit tests for pracownik.py
import unittest
from pracownik import PracownikGodzinowy
class TestPracownik(unittest.TestCase):
    def test_oblicz_pensje(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.oblicz_pensje(), 2000)
    def test_correctNameSaved(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.imie, "Piotr")
    def test_correctSurnameSaved(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.nazwisko, "Nowak")
    def test_correctStawkaSaved(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.stawkaPodstawowa, 40)
    def test_correctHoursSaved(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.przeplaconeGodziny, 50)
    def test_opis(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 50)
        self.assertEqual(obj.opis(), "Piotr Nowak")
    def test_ifZeroisZero(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 40, 0)
        self.assertEqual(obj.oblicz_pensje(), 0)
    def test_opis2(self):
        obj = PracownikGodzinowy("Adam", "Nowak", 40, 50)
        self.assertEqual(obj.opis(), "Adam Nowak")
    def test_oblicz_pensje2(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 50, 80)
        self.assertEqual(obj.oblicz_pensje(), 4000)
    def test_oblicz_pensje3(self):
        obj = PracownikGodzinowy("Piotr", "Nowak", 30, 10)
        self.assertEqual(obj.oblicz_pensje(), 300)
