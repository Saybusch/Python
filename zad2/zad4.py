budget = float(input("Podaj budżet miesięczny: "))
sum = 0.0
while True:
    try:
        enc = float(input(f"Podaj wydatek (gdy napiszesz wszystkie wydatki napisz 0 aby zakończyć program): "))
        sum += enc
    except ValueError:
        print("Błędna wartość, spróbuj ponownie")
    if enc == 0:
        break
if sum > budget:
    print(f"Przekroczyłeś budżet o {sum-budget:.2f} zł")
elif sum < budget:
    print(f"W budżecie pozostało Ci {budget-sum} zł")
else:
    print("Wydałeś cały budżet")