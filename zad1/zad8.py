start = float(input("Podaj początkową ilość organizmów: "))
przyrost = float(input("Podaj dzienny przyrost populacji: "))
dni = int(input("Przez ile dni populacja ma się rozwijać: "))
for i in range(dni):
    print(f"\nDzień: {i}, ilość organizów: {float(start):.2f}")
    start += start*przyrost/100