'''
************************************************
 nazwa:                 losuj
 opis:                  Funkcja losuje daną ilość losowych liczb od 1 do 6 i wpisuje je do tablicy
 parametry:             amount - ilość liczb do wylosowania
 zwracany typ i opis:   array (tablica) - zwraca tablicę zapełnioną wegenerowanymi losowymi liczbami
 autor:                 12345678910
************************************************
'''

import random
def losuj(amount) -> list:
    tablica = []
    for i in range(amount):
        tablica.append(random.randint(1, 6))
        print(f"Kostka {i + 1}: {tablica[i]}")
    return tablica
def licz(tablica):
    suma = 0
    for i in set(tablica):
        ilosc = tablica.count(i)
        if ilosc > 1:
            suma += i * ilosc
    return suma
if __name__ == "__main__":
    loop = True
    while loop:
        dice = 0
        while dice < 3 or dice > 10:
            dice = int(input("Ile kostek chcesz rzucić?(3 - 10)\n"))
        array = losuj(dice)
        print(f"Liczba uzyskanych punktów: {licz(array)}")
        response = input("Jeszcze raz? (t/n)\n")
        if response == "t":
            loop = True
        elif response == "n":
            loop = False