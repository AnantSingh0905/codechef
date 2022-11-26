a = int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    k=0
    while a>2:
        k+=(b+c)
        a=int(a/2)
    print(k+b)
