def kinetic_energy(weight, velocity):
    kinetic = 0.5 * weight * velocity * velocity
    return kinetic
while True:
    try:
        weight = float(input("Podaj masę ciała w kilogramach: "))
        velocity = float(input("Podaj prędkość ciała w sekundach: "))
        if weight > 0 and velocity > 0:
            print(f"Energia kinetyczna wynosi: {kinetic_energy(weight, velocity)}")
            break
        else: raise ValueError
    except ValueError:
        print("Niepoprawne dane")
