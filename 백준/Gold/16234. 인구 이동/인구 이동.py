import sys
from collections import deque

def solve():
    n, l, r = map(int, sys.stdin.readline().split())
    
    a = []
    for _ in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, 1, -1)
    
    day = 0
    
    while True:
        visited = [[False] * n for _ in range(n)]
        moved = False
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    # BFS로 연합 찾기
                    q = deque([(i, j)])
                    visited[i][j] = True
                    union = [(i, j)]
                    total = a[i][j]
                    
                    while q:
                        x, y = q.popleft()
                        
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                                diff = abs(a[x][y] - a[nx][ny])
                                if l <= diff <= r:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
                                    union.append((nx, ny))
                                    total += a[nx][ny]
                    
                    # 연합이 2개 이상이면 인구 이동
                    if len(union) > 1:
                        moved = True
                        avg = total // len(union)
                        for x, y in union:
                            a[x][y] = avg
        
        if not moved:
            break
            
        day += 1
    
    return day

print(solve())