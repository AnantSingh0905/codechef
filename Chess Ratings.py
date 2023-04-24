from math import ceil
t=int(input())
for i in range(t):
    x,y = input().split()
    x,y=int(x),int(y)
    d=int(y-x)
    d=ceil(d/8)
    print(d)
