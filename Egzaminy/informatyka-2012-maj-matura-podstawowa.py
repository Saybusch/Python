def checksum(maximum, minimum, n):
    value_max = maximum; value_min = minimum; value = n
    sum_max = 0; sum_min = 0; sum_n = 0
    while maximum > 0:
        sum_max += maximum % 10
        maximum /= 10
    while minimum > 0:
        sum_min += minimum % 10
        minimum /= 10
    while n > 0:
        sum_n += n % 10
        n /= 10
    if sum_max < sum_n:
        value_max = value
    if sum_min > sum_n:
        value_min = value
    return value_max, value_min
def checkciag(n):
    last = n % 10
    n //= 10
    while n > 0:
        if n % 10 >= last:
            return False
        last = n % 10
        n //= 10
    return True
ls = []
with open("cyfry.txt", "r") as f:
    for i in f:
        ls.append(int(i.strip()))
with open("zadanie4.txt", "w") as f:
    ls_ciag = []
    c = 0
    maxim = 0
    minim = 99999999
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            c+=1
        maxim, minim = checksum(maxim, minim, ls[i])
        if checkciag(ls[i]):
            ls_ciag.append(ls[i])
    f.write(f"1. {str(c)}\n")
    f.write(f"2. Max: {str(maxim)} Min: {str(minim)}\n")
    print(ls_ciag)
    f.write(f"3. {ls_ciag}")
