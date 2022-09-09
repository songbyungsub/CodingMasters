from sys import stdin

a=int(input())
lst=[list(map(int,stdin.readline().split())) for _ in range(a)]
for i in lst:
    if 1 not in i:
        for j in range(a):
            if i[j]==2:
                i[j]=0
cnt=0
for j in range(a):
    lis=[]
    for i in lst:  
        lis.append(i[j])
    if 1 in lis:
        for j in range(a):
            if lis[j]==2:
                cnt+=1
print(cnt)