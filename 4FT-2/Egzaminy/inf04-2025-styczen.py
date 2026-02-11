class Urzadzenia:
    def komunikat(self, message: str):
        print(message)
class Pralka(Urzadzenia):
    def __init__(self):
        self.__numerProgramuPrania = 0
    def ustawProgram(self, number: int) -> int:
        if 1 <= number <= 12:
            self.__numerProgramuPrania = number
            self.komunikat("Program został ustawiony")
        else:
            self.__numerProgramuPrania = 0
            self.komunikat("Podano niepoprawny numer programu")
        return self.__numerProgramuPrania

class Odkurzacz(Urzadzenia):
    def __init__(self):
        self.__state: bool = False
    def on(self):
        if not self.__state:
            self.__state = True
            self.komunikat("Odkurzacz włączono")
    def off(self):
        if self.__state:
            self.__state = False
            self.komunikat("Odkurzacz wyłączono")
if __name__ == "__main__":
    pralka = Pralka()
    odkurzacz = Odkurzacz()

    value = int(input("Podaj numer prania 1..12\n"))
    pralka.ustawProgram(value)

    odkurzacz.on()
    odkurzacz.on()
    odkurzacz.on()

    odkurzacz.komunikat("Odkurzacz wyładował się")

    odkurzacz.off()
