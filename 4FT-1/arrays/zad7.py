import math
import random
def sortlist(table):
    for i in range(len(table)):
        for k in range(len(table) - i - 1):
            if table[k] > table[k+1]:
                table[k], table[k+1] = table[k+1], table[k]
    return table
ls = [random.randint(1, 100) for x in range(15)]
ls_square = [round(math.sqrt(x), 2) for x in ls]
print(ls)
print(ls_square)
print(sortlist(ls))
print(sortlist(ls_square))