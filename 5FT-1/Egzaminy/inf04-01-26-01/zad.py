import random
class Kosc:
    instances = 0
    images = [f"kosc{x}.png" for x in range(7)]
    def __init__(self, inputDice=None):
        if inputDice is None:
            self.diceValue = random.randint(1, 6)
        else:
            if inputDice > 6 or inputDice < 1:
                self.diceValue = 0
            else:
                self.diceValue = inputDice
        self.fileID = self.diceValue
        self.available = True
        Kosc.instances += 1
    def throw(self):
        if self.available:
            self.diceValue = random.randint(1, 6)
            self.fileID = self.diceValue
    def block(self):
        self.available = False
    def checkValue(self):
        match self.diceValue:
            case 0:
                print("zero")
            case 1:
                print("jeden")
            case 2:
                print("dwa")
            case 3:
                print("trzy")
            case 4:
                print("cztery")
            case 5:
                print("pięć")
            case 6:
                print("sześć")
if __name__ == '__main__':
    dice1 = Kosc()
    print(f"Ilośc instancji klasy Kosc: {Kosc.instances}")
    print(f"Ilość oczek kości: {dice1.diceValue}")
    dice1.checkValue()
    print(Kosc.images[dice1.fileID])
    dice2 = Kosc(int(input("Podaj ilosc oczek na kosci: ")))
    print(f"Ilośc instancji klasy Kosc: {Kosc.instances}")
    print(f"Ilość oczek kości: {dice2.diceValue}")
    dice2.checkValue()
    print(Kosc.images[dice2.fileID])
