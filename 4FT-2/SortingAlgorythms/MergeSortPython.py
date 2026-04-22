import random
class MergeSort:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(1, 1000) for _ in range(n)]
    @staticmethod
    def conquer(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    @staticmethod
    def sortuj(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = MergeSort.sortuj(array[:mid])
        right = MergeSort.sortuj(array[mid:])
        return MergeSort.conquer(left, right)
if __name__ == "__main__":
    array = MergeSort.generuj_tablice(5)
    print(array)
    print(MergeSort.sortuj(array))