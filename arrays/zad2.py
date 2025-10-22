import random
ls = [random.randint(1, 100) for x in range(20)]
avg = sum(ls) / len(ls)
print(ls)
print(f"Największa liczba: {max(ls)}")
print(f"Najmniejsza liczba: {min(ls)}")
print(f"Średnia wszystkich wylosowanych liczb: {avg:.2f}")
e_ls = [x for x in ls if x % 2 == 0]
print(e_ls)