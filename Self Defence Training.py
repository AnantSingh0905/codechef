num = int(input())
for i in range(num):
    num_of_wm=int(input())
    list1=list(map(int,input().split()))
    count=0
    for j in range(num_of_wm):
        if list1[j]>=10 and list1[j]<=60:
            count+=1
    print(count)
