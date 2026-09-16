PIN = 1234
tries = 3
if __name__ == '__main__':
    while tries > 0:
        try:
            pin = int(input("Podaj PIN: "))
            if pin == PIN:
                print("Telefon odblokowany")
                break
            else:
                print("Niepoprawny PIN. Spróbuj ponownie.")
                tries -= 1
                if tries == 0:
                    print("Telefon zablokowany.")
        except ValueError:
            print("Pin musi składać się tylko z liczb")