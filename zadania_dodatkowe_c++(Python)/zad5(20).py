import random
def gambleTable():
    table = []
    for i in range(3):
        table.append(random.randint(10, 29))
    return table
def aveg(table):
    newls = []
    avg = 0
    for i in table:
        if i % 3 == 0:
            newls.append(i)
    for i in newls:
        avg += i
    if len(newls) != 0:
        return avg / len(newls)
    else:
        return 0
ls = gambleTable()
print(ls)
print(aveg(ls))