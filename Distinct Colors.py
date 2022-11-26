t=int(input())
while t:
    p=int(input())
    lst = list(map(int, input().strip().split()))
    k=max(lst)
    print(k)
    t=t-1
