import sys
a = int(input())

student = list()

for i in range(a):
    n, s = sys.stdin.readline().split()
    student.append([int(s), n])

student.sort(reverse=True)

for i in range(a):
    print(student[i][1], end=" ")