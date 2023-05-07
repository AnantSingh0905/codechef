a = int(input())
for i in range(a):
    a,b,c=list(map(int,input().split()))
    d=a+b+c
    for i in range(2,d):
        if a%i!=0 and b%i!=0 and c%i!=0:
            print(i)
            break
