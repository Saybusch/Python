sum = 0.0
i = 1
while i <= 10:
    try:
        sum += float(input(f"{i}. Podaj liczbę do zsumowania: "))
        i+=1
    except ValueError:
        print("Błędna wartość. Spróbuj ponownie")
print(f"Suma liczb podanych przez ciebie wynosi: {sum:.2f}")