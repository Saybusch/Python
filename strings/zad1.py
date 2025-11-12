zdanie = input("Podaj zdanie: ")
aCount = 0
zdania = zdanie.split()
print(f"Liczba słów: {len(zdania)}")
if "Python" in zdanie:
    print("Czy występuje 'Python'? Tak")
else:
    print("Czy występuje 'Python'? Nie")
print(f"Litera 'a' występuje {zdanie.count("a")} razy")
print(f"Pierwsze 'a' na pozycji {zdanie.find("a")}")
