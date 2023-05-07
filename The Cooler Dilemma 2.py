t = int(input())
for i in range(t):
    r,p=list(map(int,input().split()))
    if p%r==0:
        print(p//r-1)
    else:
        print(p//r)
