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