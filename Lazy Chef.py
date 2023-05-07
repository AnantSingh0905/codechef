t=int(input())
for i in range(t):
    a,b,c=list(map(int,input().split())) 
    k=a*b
    j=a+c
    result=min(j,k)
    print(result)
