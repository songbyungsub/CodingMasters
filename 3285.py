from dis import dis
a=int(input())
b,c=map(int,input().split())
arr=[]
for _ in range(a):
    d,e=map(int,input().split())
    arr.append((abs(b-d)+abs(c-e))*100)
print(min(arr))