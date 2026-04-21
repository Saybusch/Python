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
    def znajdz_pierwszy_z_prefiksem1(cls, prefix):
        for el in cls.napisy:
            pasuje = len(prefix) < len(el)
            for i in range(len(prefix)):
                if el[i] != prefix[i]:
                    pasuje = False
                    break
            if pasuje:
                return el
        return None
    @classmethod
    def znajdz_pierwszy_z_prefiksem2(cls, prefix):
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
    array = ["ala", "kot", "ala", "pies", "kot"]
    istota = WyszukiwanieNapisow(array)
    print(istota.zawiera("ala"))
    print(istota.indeks("kot"))
    print(istota.znajdz_wszystkie("ala"))
    print(istota.licz_wystapienia("kot"))
    print(istota.najczestszy())
    print(istota.znajdz_pierwszy_z_prefiksem1("pi"))
    print(istota.znajdz_pierwszy_z_prefiksem2("pi"))