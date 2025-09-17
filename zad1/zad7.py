def silnia(liczba, loop):
    liczba *= loop
    if loop > 1:
        return silnia(liczba, loop-1)
    return liczba
liczba = int(float(input("Podaj nieujemną liczbę całkowitą nieujemną(naturalną) aby uzyskać jej silnię: ")))
print(f"Silnia dla liczby {liczba} wynosi {silnia(liczba, liczba-1)}")