from collections import deque
import sys

# 입력 받기: 정점 수, 간선 수, 시작 정점
n, m, v = map(int, input().split())

# 그래프 초기화 (정점 번호: 1부터 n까지)
gr = [[] for _ in range(n+1)]

# 간선 정보 입력받기 (무방향 그래프이므로 양쪽에 추가)

for i in range(m):
    a , b = map(int,sys.stdin.readline().split())
    gr[a].append(b)
    gr[b].append(a)


# 각 정점의 인접 리스트를 오름차순으로 정렬 (작은 번호 우선)

for i in range(1,n+1):
    gr[i].sort()


# DFS 구현
# 방문 여부 리스트 (1-indexed)
# DFS 방문 순서 저장

visited = [False] * (n+1)
result_dfs = []

def dfs(v):
    visited[v] = True
    result_dfs.append(v)
    for nxt in gr[v]:
        if visited[nxt] == False:
            dfs(nxt)


dfs(v)
print(*result_dfs)

# 현재 정점 방문 처리
# 방문한 정점을 결과 리스트에 추가
# 시작 정점부터 DFS 수행






# BFS 구현
# BFS용 방문 여부 초기화
# BFS 방문 순서 저장
# 큐 초기화 및 시작 정점 삽입
# 시작 정점 방문 처리

visited = [False] * (n+1)
result_bfs = []

q = deque()
q.append(v)

while q:
    cur = q.popleft()
    result_bfs.append(cur)
    visited[cur] = True
    for nxt in gr[cur]:
        if visited[nxt] == False:
            visited[nxt] = True
            q.append(nxt)



print(*result_bfs)
