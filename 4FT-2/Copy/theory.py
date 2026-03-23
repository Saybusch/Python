import copy

class MojaKlasa:
    def __init__(self, d):
        self.Dana = d

p1 = MojaKlasa(1)
p2 = copy.copy(p1)
p3 = copy.deepcopy(p1)

print("p1.Dana =", p1.Dana)
print("p2.Dana =", p2.Dana)

p1.Dana = 2

print("\nWartość po zmianie obiektu p1")
print("p1.Dana =", p1.Dana)
print("p2.Dana =", p2.Dana)
print("p3.Dana =", p3.Dana)

