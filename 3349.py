import math
a=int(input())
n,m=map(int,input().split())
min=10000
flag=0
if n>=0:
    for i in range(n):
        b=math.sqrt(pow(i,2)+pow(a,2))/10 + math.sqrt(pow((i-n),2)+pow(m,2))/5
        if min > b:
            min=b
            flag=i
else:
    for i in range(n,0):
        b=math.sqrt(pow(i,2)+pow(a,2))/10 + math.sqrt(pow((i-n),2)+pow(m,2))/5
        if min >b:
            min=b
            flag=i
print(flag)