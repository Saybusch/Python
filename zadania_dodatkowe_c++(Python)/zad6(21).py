import random
def gambleTable():
    table = []
    for i in range(50):
        table.append(random.randint(0, 99))
    return table
def avgOdd(table) -> (float):
    ls = []
    suma = 0
    for i in table:
        if i % 2 != 0:
            ls.append(i)
    for i in ls:
        suma += i
    return suma / len(ls)
ls = gambleTable()
print(ls)
print(avgOdd(ls))
