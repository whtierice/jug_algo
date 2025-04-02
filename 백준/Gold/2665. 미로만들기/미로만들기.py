import sys
from collections import deque

n = int(sys.stdin.readline().strip())

miro = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
cnt = 0

def maze(miro,n):
    dist = [[0] * n for _ in range(n)]

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    
    dist[0][0] = 1

    q = deque([(0,0)])

    while q:
        a, b = q.popleft()

        if a == n-1 and b == n-1:
            break
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                if miro[nx][ny] == 1:
                    dist[nx][ny] = dist[a][b]    
                    q.appendleft((nx,ny))
                else:
                    dist[nx][ny] = dist[a][b] + 1
                    q.append((nx,ny))
                
    return dist[n-1][n-1]

ans = maze(miro,n)
print(ans-1)