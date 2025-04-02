import sys
import heapq

n, m, k, x = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

INF = float("inf")
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append((b,1))

dist = [INF] * (n+1)

q = []

heapq.heappush(q,(0,x))
dist[x] = 0

while q:
    cur_dist, cur_node = heapq.heappop(q)

    if cur_dist > dist[cur_node]:
        continue

    for nxt,w in graph[cur_node]:
        n_dist = w + dist[cur_node]
        if n_dist < dist[nxt]:
            dist[nxt] = n_dist
            heapq.heappush(q,(n_dist, nxt))

ans = []
for i in range(1,n+1):
    if dist[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    print(*ans, sep='\n')
        

