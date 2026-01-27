print("Planowany wzrost cen czesnych przez kolejne 5 lat: ")
czesne = 8000.0
for i in range(6):
    print(f"\n Rok {i}: {czesne:.2f} zł")
    czesne += 0.03 * czesne