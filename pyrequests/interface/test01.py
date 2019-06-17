profit = int(input('show me the money: '))
arr=[1000000,600000,400000,200000,100000,0]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
bonus = 0
for i in range(len(arr)):
    if profit > arr[i]:
        bonus +=(profit-arr[i])*rates[i]
        profit=arr[i]

print('your money is %d'%bonus)

