a = int(input())
for i in range(a):
    a,b=map(int,input().split())
    if (a<b):
        print(a)
    else:
        print(2*a-b)
