for i in range(int(input())):
    a,b=map(int,input().split())
    list1=list(map(int,input().split()))
    c=0
    for i in range(a):
        if ((list1[i]+b)%7==0):
            c=c+1
    print(c)
