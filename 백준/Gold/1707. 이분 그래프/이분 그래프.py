import sys
sys.setrecursionlimit(10**6)

# 어떤 정점이 있을 때 인접한 정점과 다른 색으로 칠해져있어야 함.
# 나와 연결된 노드에 나와 다른 색을 칠해라.

n = int(sys.stdin.readline().strip())


def dfs(v, col):
    for nxt in graph[v]:
        if col[nxt] == -1:
            col[nxt] = 1 - col[v]
            if not dfs(nxt, col):
                return False
        elif col[nxt] == col[v]:
            return False
    return True
            



for _ in range(n):
    m , k = list(map(int,sys.stdin.readline().split()))
    check = True
    graph = [[] for _ in range(m+1)]
    col = [-1] * (m+1)

    for _ in range(k):
        a, b = list(map(int, sys.stdin.readline().split()))
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, m+1):
        if col[i] == -1:
            col[i] = 0
            if not dfs(i, col):
                check = False
                break


    if check:
        print("YES")
    else:
        print("NO")






