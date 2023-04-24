# cook your dish here
t=int(input())
for i in range(t):
    x, y, z = input().split()
    x,y,z=int(x),int(y),int(z)
    d=int(y/x)
    if z>d:
        print(z-d)
    else:
        print(0)
