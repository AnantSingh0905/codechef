for i in range(int(input())):
    t=int(input())
    k=0
    list1=list(map(int,input().split()))
    for i in range(t):
        if list1[t-1]==0:
            t=t-1
    print(t-1)
        
