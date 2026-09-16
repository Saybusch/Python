import unittest
from kalkulator import dodaj, odejmij, pomnoz, podziel, wykonaj_dzialanie
class TestKalkulator(unittest.TestCase):
    def test_dodaj(self): self.assertEqual(dodaj(5, 3), 8)
    def test_odejmin(self): self.assertEqual(odejmij(5, 3), 2)
    def test_pomnoz(self): self.assertEqual(pomnoz(5, 3), 15)
    def test_podziel(self): self.assertEqual(podziel(6, 3), 2)
    def test_dzielenie_przez_zero(self): self.assertEqual(podziel(6, 0), "Nie można podzielić przez zero")
    def test_wybor_dodaj(self): self.assertEqual(wykonaj_dzialanie("1", 6, 3), 9)
    def test_wybor_odejmij(self): self.assertEqual(wykonaj_dzialanie("2", 6, 3), 3)
    def test_wybor_pomnoz(self): self.assertEqual(wykonaj_dzialanie("3", 6, 3), 18)
    def test_wybor_podziel(self): self.assertEqual(wykonaj_dzialanie("4", 6, 3), 2)
    def test_bledny_wybor(self): self.assertEqual(wykonaj_dzialanie("5", 6, 3), "Nieprawidłowy wybór")
