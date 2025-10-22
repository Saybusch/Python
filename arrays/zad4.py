import random
ls = [random.randint(1, 20) for x in range(8)]
print(f"Przed: {ls}")
for i in range(len(ls)-1):
    if ls[i] < 10:
        ls[i] = 0
print(f"Po: {ls}")