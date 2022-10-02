import sys

a=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
cnt={}
c=[]
d=[]
for i in lst:
    try:
        cnt[i]+=1
    except:
        cnt[i]=1
cnt=list(cnt.items())
for i in range(len(cnt)):
    if cnt[i][1]>=4:
        d.append(cnt[i][0])
        d.append(cnt[i][0])
    elif cnt[i][1]>=2:
        d.append(cnt[i][0])
for i in range(len(d)):
    for j in range(i+1,len(d)):
        c.append(d[i]*d[j])
if c: print(max(c))
else: print(0)
