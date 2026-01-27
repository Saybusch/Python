countMain = 0
def czy_pierwsza(n):
    global countMain
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    countMain += 1
    return True
def najwieksza_pierwsza_mniejsza_od(n):
    global countMain
    for i in range(n-1, 2, -1):
        print("Prime Loop interation: %i" % countMain, end="\r")
        if czy_pierwsza(i):
            return i
    return None
num = int(input("Liczba dla której szukasz największej liczby pierwszej: "))
print(najwieksza_pierwsza_mniejsza_od(num))