import unittest
from zad import Osoba
class TestOsoba(unittest.TestCase):
    def test_klasa(self):
        print(f"Liczba zarejestrowaych osób to {Osoba.instances}")
        self.assertEqual(Osoba.instances, 0)
        obj1 = Osoba()
        self.assertEqual(obj1._Osoba__id, 0)
        self.assertEqual(obj1._Osoba__imie, "")
        id_os = int(input("Podaj id: "))
        imie_os = input("Podaj imie: ")
        obj2 = Osoba(id_os, imie_os)
        self.assertEqual(obj2._Osoba__id, id_os)
        self.assertEqual(obj2._Osoba__imie, imie_os)
        obj3 = obj2.kopia()
        self.assertEqual(obj3._Osoba__id, obj2._Osoba__id)
        self.assertEqual(obj3._Osoba__imie, obj2._Osoba__imie)
        obj1.greet("Jan")
        obj2.greet("Jan")
        obj3.greet("Jan")
        print(f"Liczba zarejestrowaych osób to {Osoba.instances}")
        self.assertEqual(Osoba.instances, 3)