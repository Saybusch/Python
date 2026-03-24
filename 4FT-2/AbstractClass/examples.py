from abc import ABC, abstractmethod
class Pracownik(ABC):
    @abstractmethod
    def oblicz_pensje(self):
        pass
class PracownikEtatowy(Pracownik):
    def __init__(self, pensja):
        self.pensja = pensja
    def oblicz_pensje(self):
        return self.pensja
class Freelancer(Pracownik):
    def __init__(self, stawka, godziny):
        self.stawka = stawka
        self.godziny = godziny
    def oblicz_pensje(self):
        return self.stawka * self.godziny
Etatowy = PracownikEtatowy(240)
Freelancer = Freelancer(40, 8)
print(Etatowy.oblicz_pensje())
print(Freelancer.oblicz_pensje())
