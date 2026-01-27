import random
def gambleTable():
    table = []
    for i in range(50):
        table.append(random.randint(100, 999))
    return table
def dziesiatki(table) -> (list[int]):
    newls = []
    for i in table:
        l = i % 100
        newls.append(l // 10)
    return newls
ls = gambleTable()
print(ls)
print(dziesiatki(ls))
