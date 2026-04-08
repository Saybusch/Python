import random
class MergeSort:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(1, 1000) for _ in range(n)]
    @staticmethod
    def conquer(left, mid, right):
        global array
        n1 = mid - left + 1
        n2 = right - mid
        leftArr = array[left:left + n1]
        rightArr = array[mid+1:mid+1+n2]
        i = 0; j = 0; k = left
        while i < n1 and j < n2:
            if leftArr[i] <= rightArr[j]:
                array[k] = leftArr[i]
                i += 1
            else:
                array[k] = rightArr[j]
                j += 1
            k += 1
        while i < n1:
            array[k] = leftArr[i]
            i += 1
            k += 1
        while j < n2:
            array[k] = rightArr[j]
            j += 1
            k += 1
    @staticmethod
    def sortuj(left, right):
        global array
        if left >= right:
            return
        middle = left + (right - left) // 2
        MergeSort.sortuj(left, middle)
        MergeSort.sortuj(middle + 1, right)
        MergeSort.conquer(left, middle, right)


if __name__ == "__main__":
    array = MergeSort.generuj_tablice(999999)
    print(array)
    MergeSort.sortuj(0, len(array) - 1)
    print(array)