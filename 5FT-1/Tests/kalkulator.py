from unittest import case


def dodaj(a, b):
    return a + b
def odejmij(a, b):
    return a - b
def pomnoz(a, b):
    return a * b
def podziel(a, b):
    if b == 0:
        return "Nie można podzielić przez zero"
    return a / b
def wykonaj_dzialanie(wybor, a, b):
    match wybor:
        case "1":
            return dodaj(a, b)
        case "2":
            return odejmij(a, b)
        case "3":
            return pomnoz(a, b)
        case "4":
            return podziel(a, b)
    return "Nieprawidłowy wybór"


if __name__ == "__main__":
    print("KALKULATOR")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    wybor = input("Wybierz dzialanie: ")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print("Wynik: ", wykonaj_dzialanie(wybor, a, b))
