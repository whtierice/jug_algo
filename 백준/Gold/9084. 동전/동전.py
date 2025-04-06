import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline().strip())
    dp = [0] * (money+1)
    dp[0] = 1

    for num in nums:
        for i in range(num, money+1):
            dp[i] = dp[i] + dp[i-num]
            # i원을 만드는 방법 = 지금보다 작은 동전으로 i를 만드는 방법을 모두 더한 경우의 수와, 지금 구하려는 값에서 동전만큼 뺀 경우의 수

    print(dp[money])

