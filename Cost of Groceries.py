a = int(input())
for i in range(a):
    num,lvalue=list(map(int,input().split()))
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    cost=0
    for i in range(num):
        if list1[i]>=lvalue:
            cost+=list2[i]
    print(cost)
