a = int(input())
lst = list(map(int,input().split()))
lst_cpy = lst.copy()
lst_cpy.sort()

index = [0,0]
for i in range(a):
    if lst[i] != lst_cpy[i]:
        index[0] = i
        break
for i in range(a-1,-1,-1):
    if lst[i] != lst_cpy[i]:
        index[1] = i
        break

print(index[1]-index[0]+1)