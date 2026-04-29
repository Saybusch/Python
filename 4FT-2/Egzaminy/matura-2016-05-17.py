f = open('dane4.txt', 'r')
w = open('wyniki_6.txt', 'w')
total = maxim = last = 0
minim = int(f.readline())
siblingPair = []
for number in f:
    num = int(number)
    check = True
    for i in range(2, num):
        if num % i == 0:
            check = False
            break
    if check:
        total += 1
        if num < minim:
            minim = num
        if num > maxim:
            maxim = num
    if last in {num-2, num-1, num, num+1, num+2}:
        siblingPair.append(f"{last} i {number}")
    last = num
w.write(f"6.1 - jest {total} liczb pierwszych\n")
w.write(f"6.2 - minimalna: {minim} maksymalna: {maxim}\n")
w.write(f"6.3 - {len(siblingPair)}\n")
for sibling in siblingPair:
    w.write(f"{sibling}")
f.close()
w.close()