#2014310703 김진규 과제1

coin_500 = int(input("[the number of 500 won coins]"))
coin_100 = int(input("[the number of 100 won coins]"))
coin_50 = int(input("[the number of 50 won coins]"))
chicken = int(input("[the price of the chicken]"))
total = coin_50*50+coin_100*100+coin_500*500
n = total//chicken
x = total%chicken


print("the number of 500 won")
print(coin_500)
print("the number of 100 won")
print(coin_100)
print("the number of 50 won")
print(coin_50)
print("the price of the chicken")
print(chicken)

print(n, 'chickens! I still has', x, 'won!')

