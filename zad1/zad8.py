start = float(input("Podaj początkową ilość organizmów: "))
przyrost = int(input("Podaj dzienny przyrost populacji: "))
dni = int(input("Przez ile dni populacja ma się rozwijać: "))
for i in range(dni):
    print(f"\nDzień: {i}, ilość organizów: {int(start)}")
    start += start*przyrost/100