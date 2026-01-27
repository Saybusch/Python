def values(fat, carbs):
    print(f"W ciągu dnia spożywasz {fat+carbs:.2f} kalorii")
def main():
    while True:
        try:
            fat = float(input("Podaj ile gramów tłuszczów spożywasz w ciągu dnia: "))
            carbs = float(input("Podaj ile gramów węglowodanów spożywasz w ciągu dnia: "))
            if fat > 0 and carbs > 0:
                values(fat*9, carbs*4)
            else: raise ValueError
        except ValueError:
            print("Niepoprawne dane")
main()