a=int(input())
lst = list()

for i in range(1, a+1):
    x = list(map(int,input().split()))
    x.append(i)
    x[0] = -x[0]
    lst.append(x)
lst.sort()
for i in range(len(lst)):
    print(lst[i][3], end=" ")
print()