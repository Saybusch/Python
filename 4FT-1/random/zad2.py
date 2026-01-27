import random
def main():
    ls = []
    even = []
    suma = 0
    sumaEven = 0
    for i in range(10):
        number = random.randrange(10, 100)
        ls.append(number)
        if number % 2 == 0:
            even.append(number)
    for i in ls:
        suma += i
    for i in even:
        sumaEven += i
    print("Wygenerowane liczby: ", ls)
    print("Suma wygenerowanych liczb wynosi: ", suma, "\n")
    print("Liczby parzyste: ", even)
    print("Suma liczb parzystych wynosi: ", sumaEven)
main()