import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, sys.stdin.readline().split()))

gr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a , b = list(map(int, sys.stdin.readline().split()))
    gr[a].append(b)
    gr[b].append(a)



def dfs(v):
    visited[v] = True
    for nxt in gr[v]:
        if visited[nxt] == False:
            dfs(nxt)

ans = 0

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        ans +=1

    
print(ans)

