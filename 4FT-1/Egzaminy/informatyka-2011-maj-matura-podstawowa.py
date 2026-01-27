def palindrome(n):
    return n == n[::-1]
def ascii_sum(n):
    for letter in range(len(n) - 1):
        if ord(n[letter]) + ord(n[letter + 1]) == 220:
            return True
    return False
ls = []
with open('hasla.txt', 'r') as f:
    for line in f:
        ls.append(line.strip())
print(ls)
with open('wynik4a.txt', 'w') as f:
    even = 0; odd = 0
    for i in ls:
        if len(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    f.write(f"Parzyste: {str(even)}\nNieparzyste: {str(odd)}")
with open('wynik4b.txt', 'w') as f:
    for i in ls:
        if palindrome(i):
            f.write(i + '\n')
with open('wynik4c.txt', 'w') as f:
    for i in ls:
        if ascii_sum(i):
            f.write(i + '\n')