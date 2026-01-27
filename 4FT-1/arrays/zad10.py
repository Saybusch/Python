import random
def gamble():
    for i in range(30):
        temps.append(random.randint(-10, 35))
def analiza_temperatur(table):
    maxim = 0; minim = 36; avg = 0; length = 0
    for i in table:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i
        avg += i
        length += 1
    return maxim, minim, avg / length
def tempreratury_dodatnie(table):
    return [x for x in table if x > 0]
temps = []
gamble()
print("Lista wygenerowanych temperatur:\n",temps)
maximal, minimal, average = analiza_temperatur(temps)
print(f"\nMaksymalna tempretatura: {maximal}\nMinimalna temperatura: {minimal}\nŚrednia temperatura: {average:.2f} \n")
temps_positive = tempreratury_dodatnie(temps)
print("Lista temperatur większych od zera:\n",temps_positive)