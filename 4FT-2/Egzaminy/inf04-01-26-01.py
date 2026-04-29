import random


class Kosc:
    instanceCount = 0
    imageFileNames = ["kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
    def __init__(self, numberOnTile = None):
        if numberOnTile is None:
            randomNumber = random.randint(1, 6)
            self.numberOnTile = randomNumber
            self.imageFileIdentifier = randomNumber
        else:
            if numberOnTile not in range(1, 7):
                self.numberOnTile = 0
                self.imageFileIdentifier = 0
            else:
                self.numberOnTile = numberOnTile
                self.imageFileIdentifier = numberOnTile
        self.diceAvailable = True
        Kosc.instanceCount += 1
    def diceThrow(self):
        if self.diceAvailable:
            randomNumber = random.randint(1, 6)
            self.numberOnTile = randomNumber
            self.imageFileIdentifier = randomNumber
    def blockDice(self):
        self.diceAvailable = False
    def getDice(self):
        match self.numberOnTile:
            case 1:
                return "jeden"
            case 2:
                return "dwa"
            case 3:
                return "trzy"
            case 4:
                return "cztery"
            case 5:
                return "pięć"
            case 6:
                return "sześć"
if __name__ == "__main__":
    dice1 = Kosc()
    print(Kosc.instanceCount)
    print(dice1.numberOnTile, dice1.getDice())
    print(Kosc.imageFileNames[dice1.imageFileIdentifier])
    dice2 = Kosc(int(input("Podaj liczbę oczek od 1 do 6: ")))
    print(Kosc.instanceCount)
    print(dice2.numberOnTile, dice2.getDice())
    print(Kosc.imageFileNames[dice2.imageFileIdentifier])