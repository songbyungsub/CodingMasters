a,b=map(int,input().split())
x=int(input())
arr=[]
arr.append(b)
for i in range(x):
    c,d=map(int,input().split())
    if c in arr:
        arr.append(d)
    elif d in arr:
        arr.append(c)
print(len(set(arr)))