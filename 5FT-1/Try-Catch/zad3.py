try:
    grade = int(input("Podaj ocenę: "))
    if 0 < grade < 7:
        print(f"Wprowadzono poprawną ocenę: {grade}")
    else:
        print("Błąd: ocena musi być od 1 do 6.")
except ValueError:
    print("Ocena musi być liczbą całkowitą.")
finally:
    print("Sprawdzanie oceny zakończone")   