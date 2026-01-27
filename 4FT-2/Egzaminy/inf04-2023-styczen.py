'''
************************************************
 klasa: Notatka
 opis:  Klasa reprezentuję notatkę posiadającą tytuł i treść
 pola:  __licznik_notatek - przechowuje liczbę odpowiedzialną za identyfikowanie notatki
        __id - identyfikator notatki, który swoją wartość zdobywa od __licznik_notatek
        _tytul - tytuł notatki
        _tresc - treść notatki
 autor: 12345678910
************************************************
'''
class Notatka:
    __licznik_notatek = 0
    def __init__(self, tytul, tresc):
        Notatka.__licznik_notatek += 1
        self.__id = Notatka.__licznik_notatek
        self._tytul = tytul
        self._tresc = tresc
    def wyswietl(self):
        print(f"\n--- Notatka ---")
        print(f"Tytuł: {self._tytul}")
        print(f"Treść: {self._tresc}")
    def diagnostyka(self):
        print(f"{self.__id};{self._tytul};{self._tresc}")
if __name__ == "__main__":
    print("Program testujący działanie klasy Notatka")
    not1 = Notatka("Zakupy", "Kupić mleko, chleb i owoce.")
    not2 = Notatka("Plan dnia", "Nauka Pythona, spacer, film wieczorem.")
    print("\nWyświetlanie notatek:")
    not1.wyswietl()
    not2.wyswietl()
    print("\nDiagnostyka notatek:")
    not1.diagnostyka()
    not2.diagnostyka()

