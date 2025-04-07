import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

a = len(str1) 
b = len(str2)

dp = [[0] * (a+1) for _ in range(b+1)]


for i in range(1,b+1):
    for j in range(1,a+1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[b][a])