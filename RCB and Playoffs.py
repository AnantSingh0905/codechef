a = int(input())
for i in range(a):
    a,b,c=map(int,input().split())
    if(b-a)<(c*2) or (b-a)==(c*2):
        print("YES")
    else:
        print("NO")
