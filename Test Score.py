t =int(input())
while t:
    a,b,c = map(int,input().split())
    for i in range(0,a+1):
        if(i*b==c):
            print("YES")
            break
    else:
        print("NO")
    t=t-1
