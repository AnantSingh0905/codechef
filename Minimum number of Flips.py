for i in range(int(input())):
    k=int(input())
    list1=list(map(int,input().split()))
    one=list1.count(1)
    none=list1.count(-1)
    if(k%2==0):
        operation=(abs(one-none))//2
        print(operation)
    else:
        print("-1")
