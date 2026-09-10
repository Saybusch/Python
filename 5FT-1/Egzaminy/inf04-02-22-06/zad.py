class Osoba:
    instances = 0
    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.instances+=1
    def greet(self, arg):
        if self.__imie == "":
            print("Brak danych")
        else:
            print(f"Cześć {arg}, mam na imię {self.__imie}")
    def kopia(self):
        return Osoba(self.__id, self.__imie)
'''
if __name__ == '__main__':
    print(f"Liczba zarejestrowaych osób to {Osoba.instances}")
    obj1 = Osoba()
    obj2 = Osoba(int(input("Podaj id: ")), input("Podaj imie: "))
    obj3 = obj2.kopia()
    obj1.greet("Jan")
    obj2.greet("Jan")
    obj3.greet("Jan")
    print(f"Liczba zarejestrowaych osób to {Osoba.instances}")
'''

