a, b = map(int,input().split())
x, y = map(int,input().split())

if x >=a: 
    if y >= b:
        print('YES')
    elif b >= y and (b-y)+a <= x:
        print('YES')
    else: print('NO')
else: print('NO')