import random
ls = [random.choice([-1, 1]) * random.randint(100,999) for x in range(20)]
ls_minmax = []
def findLargest(number):
    max = 0
    min = 10
    while number > 0:
        check = number % 10
        if check < min:
            min = check
        if check > max:
            max = check
        number //= 10
    return int(min), int(max)
print(ls)
max9 = 0
min1 = 0
for i in ls:
    min, max = findLargest(abs(i))
    ls_minmax.append((min, max))
    if max == 9:
        max9 += 1
    if min == 1:
        min1 += 1
    if min == 0:
        ls.remove(i)
        ls_minmax.remove((min, max))
print(max9)
print(min1)
print(ls)
print(ls_minmax)