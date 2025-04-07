import sys

n, k = list(map(int, sys.stdin.readline().split()))
dp = [0] * (k+1)

bag = []

for i in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    bag.append((x,y))

bag.sort()


for weight, val in bag:
    for i in range(k, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight] + val)

print(dp[k])