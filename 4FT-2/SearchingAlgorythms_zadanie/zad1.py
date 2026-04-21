class WyszukiwanieNapisow:
    napisy = []
    def __init__(self, napisy:list):
        WyszukiwanieNapisow.napisy = napisy
    @classmethod
    def zawiera(cls, find) -> bool:
        print(cls.napisy)
        for el in cls.napisy:
            if el == find:
                return True
        return False
    @classmethod
    def indeks(cls, find) -> int:
        for i in range(len(cls.napisy)):
            if cls.napisy[i] in find:
                return i
        return -1
    @classmethod
    def znajdz_wszystkie(cls, find) -> list:
        return [x for x in range(len(cls.napisy)) if cls.napisy[x] == find]
    @classmethod
    def znajdz_pierwszy_z_prefiksem(cls, prefix):
        for el in cls.napisy:
            if el[:len(prefix)] == prefix:
                return el
        return None
    @classmethod
    def licz_wystapienia(cls, find):
        return len(cls.znajdz_wszystkie(find))
    @classmethod
    def najczestszy(cls):
        slownik = {x: len([_ for _ in cls.napisy if _ == x]) for x in cls.napisy}
        maxim = 0
        maximKey = ""
        for it in slownik:
            item = slownik.get(it)
            if item > maxim:
                maxim = item
                maximKey = it
        return maximKey

if __name__ == '__main__':
    '''
    amount = int(input("Ile napisów: "))
    array = []
    for i in range(1, amount+1):
        array.append(input(f"Dana {i}: "))
        if array[-1] == "" or len(array) != i:
            array.pop()
            i -= 1
    istota = WyszukiwanieNapisow(array)
    #t1 = input("Szukane słowo: ")
    if istota.zawiera(t1):
        print(f"Lista zawiera {t1}")
    else:
        print(f"Lista nie zawiera {t1}")
    print(f"Pierwszy indeks elementu {t1}: {istota.indeks(t1)}")
    print(f"Indeksy elementu {t1}: {istota.znajdz_wszystkie(t1)}")
    t2 = input("Prefiks do słów: ")
    print(f"Pierwszy napis zawierający prefiks {t2}: {istota.znajdz_pierwszy_z_prefiksem(t2)}")
    '''
    array = ["ala", "kot", "ala", "pies", "kot"]
    istota = WyszukiwanieNapisow(array)
    print(istota.zawiera("ala"))
    print(istota.indeks("kot"))
    print(istota.znajdz_wszystkie("ala"))
    print(istota.licz_wystapienia("kot"))
    print(istota.najczestszy())
    print(istota.znajdz_pierwszy_z_prefiksem("pi"))