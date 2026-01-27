ls = [45, 60, 75, 50, 90, 30, 80]
fin = []
avg = sum(ls)/len(ls)
for i in ls:
    if i > avg:
        fin.append(i)
print(f"Średnia: {round(avg, 1)}")
print(f"Uczniowie powyżej średniej: {fin}")