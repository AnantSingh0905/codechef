a = int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    rent=a*c
    if(b>rent):
        print("YES")
    else:
        print("NO")
