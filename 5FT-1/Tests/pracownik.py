class Pracownik():
    def __init__(self, imie, nazwisko, stawkaPodstawowa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawkaPodstawowa = stawkaPodstawowa
    def opis(self):
        return f"{self.imie} {self.nazwisko}"
    def oblicz_pensje(self):
        return self.stawkaPodstawowa


class PracownikGodzinowy(Pracownik):
    def __init__(self, imie, nazwisko, stawkaPodstawowa, przeplaconeGodziny):
        super().__init__(imie, nazwisko, stawkaPodstawowa)
        self.przeplaconeGodziny = przeplaconeGodziny
    def oblicz_pensje(self):
        return self.stawkaPodstawowa * self.przeplaconeGodziny


def pobierz_stawke():
    stawka = int(input("Podaj stawke podstawowa (30-80): "))
    while stawka < 30 or stawka > 80:
        print("Niepoprawna stawka, podaj jeszcze raz.")
        stawka = int(input("Podaj stawke podstawowa (30-80): "))
    return stawka
stawkaOgol = pobierz_stawke()
obj1 = PracownikGodzinowy("Piotr", "Nowak", stawkaOgol, 50)
obj2 = PracownikGodzinowy("Anna", "Nowak", stawkaOgol, 80)
obj3 = PracownikGodzinowy("Katarzyna", "Kowalska", stawkaOgol, 10)
print(f"{obj1.opis()} {obj1.oblicz_pensje()}")
print(f"{obj2.opis()} {obj2.oblicz_pensje()}")
print(f"{obj3.opis()} {obj3.oblicz_pensje()}")

