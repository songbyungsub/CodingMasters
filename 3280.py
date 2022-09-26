a=int(input())
d={}
for i in range(a):
    n,m = map(str,input().split())
    d[n]=m
k=input()
d=list(d.items())
f=0
for i in range(len(d)):
    if k == d[i][0]:
        print(d[i][1])
        f=1
        break
if f==0: print(-1)