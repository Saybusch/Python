import random

#zad 1

def armstrong_3_cyfrowe():
    ls = [x for x in range(100, 1000)]
    ls_final = []
    for x in ls:
        suma = 0
        for i in str(x):
            suma += int(i)**3
        if x == suma:
            ls_final.append(x)
    return ls_final

lista = armstrong_3_cyfrowe()
print(lista)

#zad 2

def srednia_nieparzystych():
    ls_rand = [random.randint(0, 99) for x in range(50)]
    suma = 0
    for i in ls_rand:
        if i % 2 == 1:
            suma += i
    if suma == 0:
        return None
    else:
        return suma / len(ls_rand)

print(srednia_nieparzystych())

#zad 3

def czy_pierwsza(n):
    if 2 >= n > 0:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def najwieksza_pierwsza_mniejsza_od(n):
    for i in range(n-1, 2, -1):
        if czy_pierwsza(i):
            return i
    return None

num = int(input("Liczba dla której szukasz największej liczby pierwszej: "))
print(najwieksza_pierwsza_mniejsza_od(num))