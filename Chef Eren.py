num = int(input())
for i in range (num):
    a,b,c=[int(x) for x in input().split()]
    even=(a//2)*b
    if a%2==0:
        odd=(a//2)*c
    else:
        odd=((a//2)+1)*c
    print(odd+even)
