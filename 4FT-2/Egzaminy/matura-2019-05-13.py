f = open('dane.txt', 'r')
w = open('wyniki6.txt', 'w')
ma = fe = lis = 0
wrong = []
for line in f:
    liner = line[:-1]
    if int(liner[-1]) % 2 == 0:
        fe += 1
    else:
        ma += 1
    if liner[2:4] == '11' or liner[2:4] == '31':
        lis += 1
    suma = 0
    for i in liner:
        integ = int(i)
        match integ % 4:
            case 0:
                suma += integ * 9
            case 1:
                suma += integ * 1
            case 2:
                suma += integ * 3
            case 3:
                if i is line[-2]:
                    suma += integ
                else:
                    suma += integ * 7
    if suma % 10 != 0:
        wrong.append(line)
w.write(f"6.1 - {fe} kobiet, {ma} mezczyzn\n")
w.write(f"6.2 - {lis} osob urodzilo sie w listopadzie\n")
w.write(f"6.2 - Bledne numery PESEL: \n")
for record in wrong:
    w.write(f"{record}\n")
w.close()
f.close()