import random
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