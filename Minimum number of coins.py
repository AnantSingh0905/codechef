num = int(input())
for i in range(num):
    rupees= int(input())
    coin_10=rupees//10
    remain=rupees%10
    coin_5=remain//5
    if remain%5==0:
        print(coin_10+coin_5)
    else:
        print("-1")
