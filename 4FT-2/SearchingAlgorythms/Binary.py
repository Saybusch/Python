import random
class Binary:
    @staticmethod
    def generuj_tablice_posortowana(n):
        table = [random.randint(1, 9999) for _ in range(n)]
        table.sort()
        return table
    @staticmethod
    def znajdz(l, p, find) -> int:
        global tablica
        if l > p:
            return -1
        mid = l + (p - l) // 2
        if find == tablica[mid]:
            return mid
        if find < tablica[mid]:
            return Binary.znajdz(l, mid-1, find)
        else:
            return Binary.znajdz(mid + 1, p, find)
if __name__ == "__main__":
    tablica = Binary.generuj_tablice_posortowana(999999)
    print(tablica)
    print(tablica[Binary.znajdz(0, len(tablica)-1, tablica[472475])])