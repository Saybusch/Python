def calc_average(lst):
    return sum(lst) / len(lst)

def determine_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1
lst = []
i = 0
while i < 5:
    i += 1
    try:
        value = int(input(f"[{i}] Podaj wyniki z 5 sprawdzianów: "))
        if 0 < value < 7:
            lst.append(value)
        else: raise ValueError
    except ValueError:
        print("Niepoprawne dane")
        i -= 1

for i in range(len(lst)):
    print(f"Ocena dla sprawdzianu numer {i+1} wynosi: {lst[i]}")
print(f"Średnia z 5 sprawdzianów wynosi: {calc_average(lst):.2f}")