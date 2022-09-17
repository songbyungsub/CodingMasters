from cmath import pi


a,b,c = map(int,input().split())
a_one = a * a *pi
b_one = (b * b*pi) * c

if a_one > b_one: print('NO')
else: print('YES')
