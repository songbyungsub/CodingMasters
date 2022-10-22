import math
def number(x):
    if a==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
a = int(input())
if number(a)==True:
    print("clap")
else:
    print(a)