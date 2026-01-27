import random
ls = [random.choice([-1, 1]) * random.randint(1000,9999) for x in range(60)]
def findhigherlower(number):
    if (number[0] > number[1]):
        for i in range(1, len(number) - 1):
            if (number[i] <= number[i + 1]):
                return -1
            else:
                if i == len(number) - 2:
                    return 0
    elif (number[0] < number[1]):
        for i in range(1, len(number) - 1):
            if (number[i] >= number[i + 1]):
                return -1
            else:
                if i == len(number) - 2:
                    return 1
    else:
        return -1

print(ls)
rising = 0; falling = 0; none = 0
for i in ls:
    returner = findhigherlower(str(abs(i)))
    if returner == -1:
        none +=1
    elif returner == 0:
        falling +=1
        print(i, returner)
    elif returner == 1:
        print(i, returner)
        rising +=1
print(rising, falling, none)
