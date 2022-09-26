a,b=map(int,input().split())
m=list(map(int,input().split()))
sum=[0]*(a-b+1)
for i in range(0,a-b+1):
    for j in range(b):
        if m[i+j]==0:
            sum[i]=0
            break
        sum[i]+=m[i+j]
if max(sum)==0: print("")
else: print(max(sum))