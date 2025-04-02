import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
indi = [0] * (n+1)
jng = [[0] * (n+1) for _ in range(n+1)]
q = deque()
for _ in range(m):
    a , b, c = list(map(int,sys.stdin.readline().split()))
    graph[b].append((a,c))
    indi[a] +=1

for i in range(1,n+1):
    if indi[i] == 0:
        jng[i][i] = 1
        q.append(i)

while q:
    cur = q.popleft()
    for nxt, cost in graph[cur]:
        for i in range(1,n+1):
            jng[nxt][i] += (jng[cur][i] * cost)
        indi[nxt] -=1
        if indi[nxt] == 0:
            q.append(nxt)

for i, j in enumerate(jng[n]):
    if j != 0:
        print(f"{i} {j}")