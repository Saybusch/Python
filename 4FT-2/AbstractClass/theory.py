from abc import ABC, abstractmethod
class Zwierze(ABC):
    @abstractmethod
    def wydaj_dzwiek(self):
        pass
class Pies(Zwierze):
    def wydaj_dzwiek(self):
        return "hau hau"
class Kot(Zwierze):
    def wydaj_dzwiek(self):
        return "Miau"
pies = Pies()
kot = Kot()
print(pies.wydaj_dzwiek())
print(kot.wydaj_dzwiek())