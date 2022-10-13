a,b=map(int,input().split())
x=[0]*a
for i in range(b):
    c,d=map(int,input().split())
    hu=list(map(int,input().split()))
    for i in range(d):
        x[hu[i]-1]+=int(c/d)
rt=" ".join(str(_)for _ in x)
print(rt)