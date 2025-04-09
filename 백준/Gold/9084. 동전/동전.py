import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().split()))
    
    money = int(sys.stdin.readline().strip())
    dp = [0] * (money+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin,money+1):
            dp[i] = dp[i] + dp[i-coin]
    print(dp[-1])




