import random
def gambleTable():
    table = []
    for i in range(20):
        table.append(random.randint(10, 99))
    return table
def findMin(table):
    smallest = table[0]
    index = 0
    for i in range(len(table)):
        if table[i] < smallest:
            smallest = table[i]
            index = i
    return smallest, index

if __name__ == "__main__":
    ls = gambleTable()
    print(ls)
    print("Najmniejsza wartość: ", findMin(ls)[0])
    print("Indeks najmniejszej wartości: ", findMin(ls)[1])