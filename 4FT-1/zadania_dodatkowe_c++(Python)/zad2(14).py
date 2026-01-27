import random

def gambleTable():
    table = []
    for i in range(30):
        table.append(random.randint(-100, 100))
    return table
def iloczyn(table):
    wynik = 1
    for i in table:
        if i > 0 and i % 3 == 0:
            wynik *= i
    return wynik
ls = gambleTable()
print(ls)
print(iloczyn(ls))