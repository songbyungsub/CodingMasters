a, b = map(int,input().split())
c = abs(b -a)
if b > a:
    d = (60 - b)+a
else: d = (60 - a)+b

if c > d: print(d)
else: print(c)