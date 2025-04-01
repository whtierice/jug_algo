import sys

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
isos = [0] * (n+1)
visited = [False] * (n+1)
ms = sys.stdin.readline().strip()
ans = 0

def dfs(v, isos):
    global ans
    global cnt
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            if isos[v] == 0 or cnt == 0:
                cnt+=1
                dfs(nxt,isos)
                ans+=1
            else: 
                return
            

for i in range(1,n+1):
    if ms[i-1] == '1':
        isos[i] = 1


for _ in range(n-1):
    a , b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    cnt = 0
    if isos[i] == 0:
        continue
    else:
        dfs(i, isos)
        ans+=1

print(ans)





# def dfs(v):
#     global ans
#     visited[v] = True
#     for nxt in graph[v]:
#         if not visited[nxt]:
#             ans +=1
#             dfs(nxt)