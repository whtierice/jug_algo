import sys

money = int(sys.stdin.readline().strip())
INF = float('inf')
coins = [2, 5]

dp = [INF] * (money + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, money+1):
        dp[i] = min(dp[i] , dp[i-coin] + 1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])