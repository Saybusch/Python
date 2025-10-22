import random
ls = [random.randint(1, 50) for x in range(20)]
ls_e = [x for x in ls if x % 2 == 0]
ls_o = [x for x in ls if x % 2 == 1]
print(f"{ls_e}, Ilość elementów: {len(ls_e)}")
print(f"{ls_o}, Ilość elementów: {len(ls_o)}")