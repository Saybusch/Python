waga = float(input("Podaj swoją wagę początkową (w kilogramach): "))
print("Przy ograniczeniu kalorii do 500 dziennie waga przez najbliższe pół roku będzie wyglądać następująco: \n")
for i in range(13):
    print(f"Waga w miesiącu: {i} wyniesie {waga:.2f} \n")
    waga -= 2.0