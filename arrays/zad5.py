import random
def gamble():
    table = [random.randint(100, 999) for x in range(20)]
    for i in range(20):
        table.append(random.randint(1000, 9999))
    return table
def sum_of_number(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def check_if_zero(number):
    while number > 0:
        if number % 10 == 0:
            return True
        number //= 10
    return False

ls = gamble()
ls_sum = []
ls_zero = [x for x in ls if check_if_zero(x)]
for i in ls:
    ls_sum.append(sum_of_number(i))

print("Liczby: ", ls)
print("Sumy liczb: ", ls_sum)
print("Parzyste sumy", [x for x in ls_sum if x % 2 == 0])
print("Nieparzyste sumy", [x for x in ls_sum if x % 2 == 1])
print("Liczby zawierające 0: ", ls_zero)
print("Podsumowanie:", sum(ls_sum))
