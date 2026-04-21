import random
class BogoSort:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(1, 1000) for _ in range(n)]
    @staticmethod
    def scramble(array):
        length = len(array) - 1
        for i in range(length):
            [array[random.randint(0, length)], array[random.randint(0, length)]] = [array[random.randint(0, length)], array[random.randint(0, length)]]
        print(array)
        return array
    @staticmethod
    def sortuj(array):
        sorting = False
        while not sorting:
            for i in range(len(array) - 2):
                if array[i] <= array[i+1]:
                    sorting = True
                else:
                    sorting = False
            if not sorting:
                BogoSort.scramble(array)
        return array
if __name__ == "__main__":
    tablica = BogoSort.generuj_tablice(4)
    print(tablica)
    print(BogoSort.sortuj(tablica))