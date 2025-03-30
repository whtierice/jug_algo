import sys

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a , b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

ans = 0

def dfs(v):
    global ans
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            ans +=1
            dfs(nxt)


dfs(1)

print(ans)
