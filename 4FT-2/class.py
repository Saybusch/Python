class Person:
    def __init__(self, name, age, salary):
        self.name = name                            #public
        self._age = age                             #protected (konwencja)
        self.__salary = salary                      #private (name mangling)
    def introduce(self):
        print(f"Cześć, mam na imię {self.name}.")
        self._show_age()                           #można używać protected wewnątrz klasy
        self.__show_salary()                        #private też jest dostępny w środku
    def _show_age(self):
        print(f"Mam {self._age} lat.")

    def __show_salary(self):
        print(f"Moja pensja to {self.__salary} zł.")

if __name__ == '__main__':
    person = Person("Jan", 25, 5000)
    #Publiczne: dostępne normalnie
    print(person.name)
    person.introduce()

    #Protected: dostęp technicznie możliwy, ale niezalecany
    print(person._age)
    person._show_age()

    #Private: normalnie nie działa
    #print(person.__salary)
    #person.__show_salary