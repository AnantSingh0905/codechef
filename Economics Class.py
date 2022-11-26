a = int(input())
for i in range(a):
    f = int(input())
    cost=0
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    for i in range(f):
        if list1[i]==list2[i]:
            cost+=1
    print(cost)
