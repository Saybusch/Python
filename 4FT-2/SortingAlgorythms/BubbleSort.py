import random
class BubbleSort:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(0, 1000) for x in range(n)]
    @staticmethod
    def sortuj(tablica):
        length = len(tablica)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if tablica[j] > tablica[j + 1]:
                    tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                    print("Zamiania: ", tablica[j], tablica[j + 1])
        return tablica
if __name__ == "__main__":
    print(BubbleSort.sortuj(BubbleSort.generuj_tablice(5)))