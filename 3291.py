a=list(map(int,input().split()))
lst=[]
for i in range(len(a)):
    if a[i]==2 and i==0:
        lst.append('L')
        continue
    if a[i]==1:
        lst.append('L')
    elif a[i]==3:
        lst.append('R')
    else:
        if lst[-1]=='L':
            lst.append('R')
        else:
            lst.append('L')
lst=' '.join(lst)
print(lst)