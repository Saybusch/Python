sum = 0
for i in range(1, 31):
    sum += 4.2
    if i == 10 or i == 15 or i == 20 or i == 25 or i == 30:
        print(f"Po przebiegnięciu {i} minut spalisz {sum:.2f} kalorii")