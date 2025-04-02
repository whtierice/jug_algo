import sys
sys.setrecursionlimit(10**6)

# 노드마다 처음 방문할 때 색상 부여
# 어떤 정점이 있을 때 인접한 정점과 다른 색으로 칠해져있어야 함.
# 나와 연결된 노드에 나와 다른 색을 칠해라.

x = int(sys.stdin.readline().strip())

        
def dfs(v):
    for nxt in graph[v]:
        if col[nxt] == -1:
            col[nxt] = 1 - col[v]
            if not dfs(nxt):
                return False
        else:
            if col[nxt] == col[v]:
                return False
    return True
            

for _ in range(x):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    graph = [[] for _ in range(a+1)]
    col = [-1] * (a+1)
    check = True

    for _ in range(b):
        q, w = list(map(int, sys.stdin.readline().split()))
        graph[q].append(w)
        graph[w].append(q)

    for i in range(0,a+1):
        if col[i] == -1:
            col[i] = 0
            if not dfs(i):
                check = False
                break
    
    if check:
        print('YES')
    else:
        print('NO')














