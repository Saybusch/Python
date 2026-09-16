balance = 1000
try:
    deposit = int(input("Podaj kwotę do wypłaty: "))
    if deposit <= 0:
        print("Kwota musi być większa od zera")
    elif deposit > balance:
        print("Brak środków na koncie")
    elif deposit % 10 != 0:
        print("Kwota do wypłaty musi być wielokrotnością 10")
    else:
        balance -= deposit
        print(f"Pozostałe saldo: {balance}")
except ValueError:
    print("Kwota musi być liczbą")
finally:
    print("Operacja zakończona")
