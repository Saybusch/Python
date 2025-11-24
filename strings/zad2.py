print("\nZadanie 1")
wiadomosci = [
    "A9X3DRozpoczecie_proceduryW",
    "B7Q1FAlpha_konfiguracjaI",
    "C2M9ZRdzen_przegrzanyW"
]
for i in wiadomosci:
    trop = i[1]
    kategoria = i[-1]
    tresc = i[5:-1]
    archiwum = (i[:5])[::-1]
    print(f"Archiwum: {archiwum}\nTrop: {trop}\nKategoria: {kategoria}\nTreść: {tresc}")
    print("-" * 30)
print("\nZadanie 2")
wiadomosc = "XqrYtajWtoMjestZprawdzBajecznyKkodWzlokalizujEartefakt"
print("Słowo klucz:", wiadomosc[3::2])
print("Miejsce ukrycia artefaktu:", wiadomosc[:15:-1])
print("Tajna wskazówka:", wiadomosc[10:30])
print(wiadomosc[0], wiadomosc[-1], wiadomosc[-2])
print("\nZadanie 3")
slowo1 = "kot"; slowo2 = "mysz"; liczba = 2025
haslo = slowo1 + slowo2 + str(liczba)
print(haslo)
haslo = haslo.upper()
print(haslo)
haslo = haslo + "!" * 5
print(haslo)
print("\nZadanie 4")
zdanie = "Python dla inżynierów jest świetny i przyjemny"
print(zdanie.split())
print(zdanie.split("i"))
print(".".join(zdanie.split()))

print("\nZadanie 5")
wiadomosc2 = (
    "„Wszystkie zwierzęta są równe, ale niektóre zwierzęta są równiejsze od innych.” "
    "To znany cytat z książki George’a Orwella „Folwark zwierzęcy”. "
    "Wielu czytelników uważa, że Orwell w mistrzowski sposób ukazuje mechanizmy władzy, "
    "ale Twain też miał swoje mądre spostrzeżenia na temat społeczeństwa." )
if "Orwell" in wiadomosc2:
    wiadomosc2.replace("Orwell", "******")
    print(wiadomosc2.replace("Orwell", "******"))
print(wiadomosc2.count("e"))