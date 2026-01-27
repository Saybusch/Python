iloscSztuk = 0
while iloscSztuk <= 0:
    iloscSztuk = int(input("Podaj ilosc sztuk oprogramowania, aby uzyskac rabat: "))
    if iloscSztuk < 0:
        print("Niepoprawna ilosc sztuk.")
if iloscSztuk < 20:
    koszt = 99 * iloscSztuk
    rabat = 0.1 * koszt
elif iloscSztuk < 50:
    koszt = 99 * iloscSztuk
    rabat = 0.2 * koszt
elif iloscSztuk < 100:
    koszt = 99 * iloscSztuk
    rabat = 0.3 * koszt
elif iloscSztuk >= 100:
    koszt = 99 * iloscSztuk
    rabat = 0.4 * koszt

print(f"Twoj rabat wyniosl: {rabat:.2f}. Kost calkowity po rabacie: {koszt-rabat:.2f}")