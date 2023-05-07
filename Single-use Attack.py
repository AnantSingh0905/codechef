# cook your dish here
t = int(input())
for oi in range(t):
    H,X,Y=list(map(int,input().split()))
    count=0
    H=H-Y
    count=1
    while (H>0):
        H=H-X
        count+=1
    print(count)
        
