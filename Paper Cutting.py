t = int(input())
for i in range(t):
    result = 0
    a,b=list(map(int,input().split()))
    result=(a//b)
    print(result*result)
