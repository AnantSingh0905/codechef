# cook your dish here
num = int(input())
for i in range (num):
    a,b,c,d=[int(x) for x in input().split()]
    e=a-b-c
    if (e)>d:
        print("0")
    elif (e+b)>d or (e+c)>d:
        print("1")
    else:
        print("2")
