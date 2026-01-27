print("Obliczanie ilosci winorosli")
odlegloscMiedzyKrzewami = 0.0
dlugoscRzedu = 0.0
miejsceNaStelaz = 0.0
while odlegloscMiedzyKrzewami <= 0.0 or dlugoscRzedu < 2*miejsceNaStelaz:
    dlugoscRzedu = float(input("Podaj w metrach dlugosc rzedu: "))
    miejsceNaStelaz = float(input("Podaj w metrach ilosc miejsca wymaganego przez stelaz: "))
    odlegloscMiedzyKrzewami = float(input("Podaj w metrach odleglosc miedzy krzewami: "))
    if odlegloscMiedzyKrzewami <= 0.0 or dlugoscRzedu < 2*miejsceNaStelaz:
        print("Niepoprawne dane")
miejsce = (dlugoscRzedu - 2*miejsceNaStelaz) / odlegloscMiedzyKrzewami
print(f"Ilosc krzewow, ktore mozna umiescic w rzedzie wynosi: {int(miejsce)}")