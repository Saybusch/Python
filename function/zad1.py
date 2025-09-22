def miles(kilometr):
    return kilometr * 0.6214

def main():
    value = float(input("Podaj liczbę kilometrów: "))
    print(f"Wartość w milach wynosi: {miles(value):.2f}")
main()