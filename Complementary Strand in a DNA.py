t=int(input())
for i in range(t):
    num=int(input())
    x = input()
    st=""
    for j in range(num):
        if x[j]=="A":
            st=st+'T'
        elif x[j]=="T":
            st=st+'A'
        elif x[j]=="C":
            st=st+'G'
        elif x[j]=="G":
            st=st+'C'
    print(st)
