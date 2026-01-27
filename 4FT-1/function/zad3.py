def szacowana(real):
    return real * 0.6
def podatek(value):
    return value * 0.0072
def main():
    while True:
        try:
            real = float(input("Podaj rzeczywistą wartość nieruchomości: "))
            if real > 0:
                print(f"Szacowana wartość nieruchomości wynosi: {szacowana(real):.2f} zł")
                print(f"Podatek od nieruchomości wynosi: {podatek(szacowana(real)):.2f} zł")
                break
            else: raise ValueError
        except ValueError:
            print("Niepoprawne dane")
main()