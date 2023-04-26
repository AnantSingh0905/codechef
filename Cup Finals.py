num = int(input())
for i in range(num):
    a,b,c=map(int,input().split())
    diff=abs(a-b)
    if diff>c:
        print("NO")
    else:
        print("YES")
