a = list(map(int,input().strip().split()))
list1=a[:-1]
if a[-1] in list1:
    print("YES")
else:
    print("NO")
