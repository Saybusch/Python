import random
def DiceThrow():
    ls = []
    for i in range(2):
        number = random.randint(1, 6)
        ls.append(number)
    print(ls)
def main():
    times = int(input("Podaj ilość rzutów kością: "))
    check = True
    while check:
        for i in range(times):
            DiceThrow()
        ans = input("Czy chcesz grać dalej? : ")
        if ans == "N":
            check = False
if __name__ == "__main__":
    main()