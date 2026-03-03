class Samochod:
    liczba_samochodow = 0
    def __init__(self, marka, przebieg):
        self.marka = marka
        self.przebieg = przebieg
        Samochod.liczba_samochodow += 1
    def pokaz_info(self):
        print(f"Marka: {self.marka}, Przebieg: {self.przebieg}km")
    def dodaj_przebieg(self, km):
        if km <= 0:
            print("Nie mozna dodać ujemnego przebiegu")
        self.przebieg += km
    @staticmethod
    def czy_duzy_przebieg(przebieg):
        return przebieg > 200000
if __name__ == '__main__':
    auto1 = Samochod("Toyota", 150000)
    auto2 = Samochod("BMW", 250000)
    auto1.pokaz_info()
    auto1.dodaj_przebieg(5000)
    auto1.pokaz_info()
    print(Samochod.liczba_samochodow)
    if Samochod.czy_duzy_przebieg(auto2.przebieg):
        print("Auto 2 ma duży przebieg")
    else:
        print("Auto 2 nie ma dużego przebiegu")

