import random

class Tablica:
    '''
    /********************************************************
    * nazwa funkcji:        sortarray
    * parametry wejściowe:  self - obiekt klasy
                            ls - tabela liczb całkowitych wpisanych z klawiatury
    * wartość zwracana:     ls - posortowana tabela liczb całkowitych wpisanych z klawiatury
    * autor:                12345678910
    * ****************************************************/
    '''
    def sortarray(self, ls):
        for i in range(len(ls) - 1):
            max = self.findmaxconditonal(ls, i)
            tmp = ls[i]
            ls[i] = ls[max]
            ls[max] = tmp
        return ls

    '''
    /********************************************************
    * nazwa funkcji:        findmaxconditonal
    * parametry wejściowe:  self - obiekt klasy
                            ls - tabela liczb całkowitych
                            left - początek przedziału / iterator funkcji sortarray
    * wartość zwracana:     maxim - indeks wartości maksymalnej z przedziału od left do długości tablicy
    * autor:                12345678910
    * ****************************************************/
    '''
    def findmaxconditonal(self, ls, left):
        maxim = left
        for j in range(left, len(ls)):
            if ls[j] > ls[maxim]:
                maxim = j
        return maxim



array = []
for i in range(1, 11):
    array.append(int(input(f"{i}. liczba: ")))
print(array)
table = Tablica()
print(table.sortarray(array))
