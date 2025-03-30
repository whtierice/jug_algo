from collections import deque
import sys

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for i in range(n-1):
    a , b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
parent = [0] * (n+1)

while q:
    cur = q.popleft()
    visited[cur] = True
    for nxt in graph[cur]:
        if visited[nxt] == False:
            parent[nxt] = cur
            visited[nxt] = True
            q.append(nxt)
            
for i in range(2, n+1):
    print(parent[i])



