import random
def multip_of_number(number):
    ans = 1
    while number > 0:
        ans *= number % 10
        number //= 10
    return ans
def maxim(array):
    max = 0
    index = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            index = i
    return index
ls = [random.randint(1000, 9999) for x in range(25)]
ls_multi = [multip_of_number(x) for x in ls]
print("Liczby: ", ls)
print("Iloczyny liczb: ", ls_multi)
print("Iloczyny większe od 50: ", [x for x in ls_multi if x > 50])
print("Iloczyny mniejsze lub równe 50: ", [x for x in ls_multi if x <= 50])
print("Maksymalny iloczyn: ", ls[maxim(ls_multi)])
for x in ls_multi:
    try:
        ls_multi.remove(0)
    except ValueError:
        break
print("Tablica po usunięciu zer: ", ls_multi)