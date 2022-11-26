a=int(input())
for i in range(a):
    a,b=map(int,input().split())
    a=a+b
    for t in range(2,a):
        if(a%t)==0:
            print("Bob")
            break
    else:
        print("Alice")
