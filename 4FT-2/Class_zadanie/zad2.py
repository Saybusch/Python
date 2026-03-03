class Bilet:
    def __init__(self, imie, nazwisko, cena):
        self._imie = imie
        self._nazwisko = nazwisko
        self.__cena = cena
    def _dane_klienta(self):
        return f"{self._imie} {self._nazwisko}"
    def cena_biletu(self):
        return self.__cena
class BiletUlgowy(Bilet):
    def __init__(self, imie, nazwisko, cena, znizka):
        super().__init__(imie, nazwisko, cena)
        self._znizka = znizka
    def cena_biletu(self):
        return round(super().cena_biletu() * (1 - self._znizka / 100), 2)
def pobierz_cene():
    cena = 0
    while not 10 <= cena <= 50:
        try:
            cena = int(input("Podaj cena: "))
        except ValueError:
            print("Niepoprawna wartość")
    return cena
if __name__ == "__main__":
    price = pobierz_cene()
    jan = BiletUlgowy("Jan", "Kowalski", price, 20)
    anna = BiletUlgowy("Anna", "Nowak", price, 50)
    print("\n---- Jan ----\n")
    print(jan._dane_klienta())
    print(f"{jan.cena_biletu()}zł")
    print("\n---- Anna ----\n")
    print(anna._dane_klienta())
    print(f"{anna.cena_biletu()}zł")
