import random
ls = [random.choice([-1, 1]) * random.randint(1000,9999) for x in range(30)]
def findhigherlower(number):
    check = number % 10
    number //= 10
    next = number % 10
    if check > next:
        while number > 0:
            check = number % 10
            if check < next:
                number //= 10
                continue
            elif check > next:
                return -1
        return 1
    elif check < next:
        while number > 0:
            check = number % 10
            if check > next:
                number //= 10
                continue
            elif check < next:
                return -1
        return 0
    else:
        return -1

print(ls)
higher = 0; lower = 0; none = 0
for i in ls:
    returner = findhigherlower(abs(i))
    if returner == -1:
        none +=1
    elif returner == 0:
        lower +=1
    elif returner == 1:
        higher +=1
print(higher, lower, none)
