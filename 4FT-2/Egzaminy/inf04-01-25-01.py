import random
class Klasa:
    __lista = []
    __length_of_lista = len(__lista)
    def __init__(self, size):
        Klasa.__length_of_lista = size
        Klasa.__lista = [random.randint(1, 1000) for _ in range(size)]
    @classmethod
    def show_elements(cls):
        [print(f"{i}: {cls.__lista[i]}") for i in range(len(cls.__lista))]
    @classmethod
    def find_first_instance_of_element(cls, element):
        try:
            return [cls.__lista.index(element)]
        except ValueError:
            return -1
    @classmethod
    def get_odd_numbers(cls):
        arr = [x for x in cls.__lista if x % 2 == 1]
        [print(x) for x in arr]
        return len(arr)
    @classmethod
    def get_average(cls):
        suma = 0
        for x in cls.__lista:
            suma += x
        return suma / cls.__length_of_lista
if __name__ == '__main__':
    obiekt = Klasa(50)
    obiekt.show_elements()
    instance = obiekt.find_first_instance_of_element(100)
    if instance != -1:
        print(f"Indeks elementu {100}: {instance}")
    print(f"Razem nieparzystych: {obiekt.get_odd_numbers()}")
    print(f"Średnia wszystkich elementów: {obiekt.get_average()}")