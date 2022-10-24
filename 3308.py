a = int(input())
if a < 4: print(0)
else:
    i = 4
    b = 0
    result = 0
    while i != a+1:
        if i % 4 == 0:
            b += 1
            result = b**2
        elif i % 4 == 2:
            result += b
        print(result)
        i += 1
print(result)