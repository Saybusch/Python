'''
*****************
nazwa funkcji:          sito

parametry wejściowe:              tab - Tablica wypełniona wartościami True oprócz indeksów 0 i 1
                        n - ostatnia liczba, którą sprawdzamy w kontekście liczb pierwszych
wartość zwracana:    liczby całkowita dodatnie będące liczbami pierwszymi

informacje:           Funkcja oblicza liczby pierwsze z przedziału od 2 do N (tutaj 100)

autor:                  12345678910

*****************
'''
def sito(tab, n):
    for i in range(2, int(n**0.5)+1):
        if tab[i]:
            for j in range(i+i, n-1, i):
                tab[j] = False
    print("Liczby pierwsze: ")
    for i in range(2, len(tab)-1):
        if tab[i]:
            print(i, end=" ")
start = 100
ls = [True] * start
ls[0] = False
ls [1] = False
sito(ls, start)