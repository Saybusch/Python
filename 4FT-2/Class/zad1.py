class Prostokat:
    __largest = 0
    def __init__(self, dlugosc, szerokosc):
        self.__dlugosc = dlugosc
        self.__szerokosc = szerokosc
    def prezentuj(self):
        print(f"Powierzchnia {self.__powierzchnia()}")
        print(f"Obwód {self.__obwod()}")
    def __powierzchnia(self):
        powi = self.__dlugosc * self.__szerokosc
        if powi > Prostokat.__largest:
            Prostokat.__largest = powi
        return powi
    def __obwod(self):
        return 2*(self.__dlugosc + self.__szerokosc)
    @staticmethod
    def largest():
        print(f"Największa powierzchnia: {Prostokat.__largest}")
if __name__ == "__main__":
    prostokaty = [
        Prostokat(10, 300),
        Prostokat(11, 21),
        Prostokat(12, 22)
    ]
    for prostokat in prostokaty:
        prostokat.prezentuj()
    Prostokat.largest()