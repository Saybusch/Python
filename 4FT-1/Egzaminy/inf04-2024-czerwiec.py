import random
def gamble(max):
    tab = []
    for i in range(max):
        tab.append(random.randint(1, 6))
        print(f"Kostka {i + 1}: {tab[i]}")
    return tab
def countPoints(tab):
    suma = 0
    for i in set(tab):
        ile_razy = tab.count(i)
        if ile_razy > 1:
            suma += ile_razy * i
    return suma

n = 0
ls = []
sum = 0
while  10 > n < 3:
    n = int(input("Podaj liczbę kostek do rzucenia (3 - 10)\n"))
ans = 't'
while ans == 't':
    sum = countPoints(gamble(n))
    print(f"Liczba uzyskanych punktów: {sum}")
    ans = input("Jeszcze raz? (t/n) \n")
