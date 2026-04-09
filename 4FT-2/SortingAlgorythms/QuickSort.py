import random
class QuickSort:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(1, 1000) for _ in range(n)]
    @staticmethod
    def sortuj(array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        lower = []; equal = []; higher = []
        for i in array:
            if i < pivot:
                lower.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                higher.append(i)
        left_arr = QuickSort.sortuj(lower)
        right_arr = QuickSort.sortuj(higher)
        return left_arr + equal + right_arr
if __name__ == "__main__":
    tablica = QuickSort.generuj_tablice(999999)
    print(tablica)
    QuickSort.sortuj(tablica)
    print(tablica)