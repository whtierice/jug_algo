import sys

n = int(sys.stdin.readline().strip())
INF = float('inf')
graph = [] * (n) 

for i in range(n):
    a, b = list(map(int,sys.stdin.readline().split()))
    graph.append((a,b))


dp = [[INF] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for length in range (2,n+1):
    for i in range(n - length + 1):
        j = i + length -1
        for k in range(i,j):
            cost = graph[i][0] * graph[k][1] * graph[j][1]
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost)
            # 행렬 i에서 j까지의 최소 연산 횟수
            # 중간을 k로 나누어서 i~k까지, k+1~j까지 구한 뒤
            # 각 행렬의 연산결과로 생긴 행렬에 대한 값 더하기.
            
print(dp[0][n-1])