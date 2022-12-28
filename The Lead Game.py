max1=0
player=0
p1=0
p2=0
for i in range(int(input())):
    p,q = map(int,input().split())
    p1+=p
    p2+=q
    value=abs(p1-p2)
    if value > max1:
        max1=value
        if p1>p2:
            player=1
        else:
            player=2
print(player,max1)
