a = 1
while a <= 100:
    b = a % 10
    c = a % 7
    d = a // 10
    if (d != 7) and (b != 7) and (c !=0):
        print(a)
    a += 1
