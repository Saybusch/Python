import random
def gambleTable():
    table = []
    for i in range(10):
        table.append(random.randint(10, 999))
    return table
def rework(table) -> (list[int]):
    newls = []
    for i in table:
        suma = 0
        while i != 0:
            suma += i % 10
            i //= 10
        newls.append(suma)
    return newls
if __name__ == '__main__':
    ls = gambleTable()
    print(ls)
    ls2 = rework(ls)
    print(ls2)
    print(sum(ls2))