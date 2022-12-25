for i in range(int(input())):
    list1=list(map(int,input().split()))
    cost=sum(list1)-min(list1)
    print(cost)
    
