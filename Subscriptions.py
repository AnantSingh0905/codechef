a = int(input())
for i in range(a):
    c,d=map(int,input().split())
    q=c//6
    p=0
    if(c%6)!=0:
        p=1
    cost=p*d+q*d
    print(cost)
