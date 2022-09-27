a,b=map(int,input().split())
'''x=[list(map(int,input().split()) for _ in range(a)]'''
x=[[0]*100 for i in range(100)]
for i in range(a):
    x[i]=list(map(int,input().split()))
lst=[]
for i in range(a):
    for j in range(b):
        if i ==0 and j==0:
            sum=x[0][0]+x[0][1]+x[1][0]
        elif i ==0 and j==b-1:
            sum=x[0][b-1]+x[0][b-2]+x[1][b-1]
        elif i==a-1 and j==0:
            sum=x[a-1][0]+x[a-1][1]+x[a-2][0]
        elif i==a-1 and j==b-1:
            sum=x[a-1][b-1]+x[a-1][b-2]+x[a-2][b-1]
        elif i==0:
            sum=x[0][j]+x[0][j-1]+x[0][j+1]+x[1][j]
        elif i==a-1:
            sum=x[a-1][j]+x[a-1][j-1]+x[a-1][j+1]+x[a-2][j]
        elif j==0:
            sum=x[i][0]+x[i-1][0]+x[i+1][0]+x[i][1]
        elif j==b-1:
            sum=x[i][b-1]+x[i-1][b-1]+x[i+1][b-1]+x[i][b-2]
        else:
            sum=x[i][j]+x[i-1][j]+x[i][j-1]+x[i][j+1]+x[i+1][j]
        lst.append(sum)
print(max(lst))