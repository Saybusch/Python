def is_prime(liczba :int) -> bool:
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return False
    return True
lst = []
for i in range(1, 101):
    if is_prime(i):
        lst.append(i)
print(lst)
'''
try:
    liczba = int(input("Podaj liczbę aby sprawdzić czy jest pierwsza: "))
    if liczba > 0:
        if is_prime(liczba):
            print(f"{liczba} jest pierwsza")
        else:
            print(f"{liczba} nie jest pierwsza")
    else:
        raise ValueError
except ValueError:
    print("Niepoprawna liczba")
'''
