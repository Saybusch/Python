'''
*****************
nazwa funkcji:          NWD
opis funkcji:           Funkcja oblicza największy wspólny dzielnik dla dwóch liczb a i b
parametry:              a - pierwsza liczba całkowita, dla której szukamy NWD
                        b - druga liczba całkowita, dla której szukamy NWD
zwracany typ i opis:    liczba całkowita dodatnia - Największy wspólny dzielnik dla podanych liczb (NWD)
autor:                  12345678910

*****************
'''
def NWD(a, b) -> int:
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
first = int(input("Podaj 1 liczbę: "))
second = int(input("Podaj 2 liczbę: "))
if first < 0 or second < 0:
    print("Niepoprawne dane")
else:
    print("NWD liczb ",first," i ",second," wynosi: ",NWD(first,second))