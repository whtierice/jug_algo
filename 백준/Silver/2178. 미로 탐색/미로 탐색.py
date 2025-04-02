from collections import deque
import sys

n, m = list(map(int, sys.stdin.readline().split()))
miro = [sys.stdin.readline().strip() for _ in range(n)]

check = [[0] * m for _ in range(n)]

q = deque([(0,0)])
check[0][0] = 1

dx = [1,-1,0,0]
dy = [0,0,-1,1]



while q:
    (x,y) = q.popleft()

    if x == n-1 and y == m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == '1' and check[nx][ny] == 0:
            check[nx][ny] = check[x][y] + 1
            q.append((nx,ny))


print(check[n-1][m-1])




