a = int(input())
b = input()
week = ['MON','TUE','WEN','THU','FRI','SAT','SUN']
id = week.index(b)
c = id + a
if c >= 7:
    c %= 7
print(week[c])
