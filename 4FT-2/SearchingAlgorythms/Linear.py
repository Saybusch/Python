import random
class Linear:
    @staticmethod
    def generuj_tablice(n):
        return [random.randint(1, 9999) for _ in range(n)]
    @staticmethod
    def znajdz(array, find) -> int:
        return [x for x in array if x == find][0]
if __name__ == "__main__":
    tablica = Linear.generuj_tablice(999999)
    print(tablica)
    print(Linear.znajdz(tablica, tablica[472475]))