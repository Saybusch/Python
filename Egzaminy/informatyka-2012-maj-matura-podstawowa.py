def checksum(maximum, minimum, n):
    sum_max = 0; sum_min = 0; sum_n = 0
    for x in str(maximum):
        sum_max += int(x)
    for x in str(minimum):
        sum_min += int(x)
    for x in str(n):
        sum_n += int(x)
    if sum_max < sum_n:
        maximum = n
    if sum_min > sum_n:
        minimum = n
    return maximum, minimum
def checkciag(n):
    for x in range(len(n) - 1):
        if n[x] >= n[x + 1]:
            return False
    return True
ls = []
with open("cyfry.txt", "r") as f:
    for i in f:
        ls.append(int(i.strip()))
with open("zadanie4.txt", "w") as f:
    ls_ciag = []
    c = 0
    maxim = 0
    minim = 9**99
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            c+=1
        maxim, minim = checksum(maxim, minim, ls[i])
        if checkciag(str(ls[i])):
            ls_ciag.append(str(ls[i]))
    f.write(f"1. {str(c)}\n")
    f.write(f"2. Max: {str(maxim)} Min: {str(minim)}\n")
    f.write(f"3. {", ".join(ls_ciag)}")