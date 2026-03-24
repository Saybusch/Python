import random
if __name__ == "__main__":
    array = []
    dice = 0
    suma = 0
    while 3 < dice > 6:
        dice = int(input("Ile kostek chcesz rzucić?(3 - 10)"))
        for i in range(dice):
            array.append(random.randint(1, 6))
            print(f"Kostak {i}: {array[i]}")
        for i in range(1, 6):
            ilosc = array.count(i)
            if ilosc > 1:
                suma += i * ilosc
    print(suma)
