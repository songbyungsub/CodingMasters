from decimal import Decimal,getcontext

n,m = map(float, input().split())

a = int(input())
getcontext().prec = a
i = Decimal(n)/Decimal(m)
i = str(i)

print(i.ljust(a+2,'0'))