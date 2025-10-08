import random
def gambleTable():
    table = []
    for i in range(50):
        table.append(random.randint(-20, 19))
    return table
def each(table):
    less = 0; equal = 0; more = 0
    for i in table:
        if i < 0:
            less += 1
        elif i == 0:
            equal += 1
        else:
            more += 1
    return less, equal, more
ls = gambleTable()
print(ls)
print(each(ls))