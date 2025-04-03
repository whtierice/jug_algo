from collections import deque
import sys

n = int(sys.stdin.readline().strip())
miro = [sys.stdin.readline().strip() for _ in range(n)]

check = [[0] * n for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])
    check[x][y] = 1
    while q:
        (x,y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0:
                if miro[nx][ny] == '1':
                    check[nx][ny] = 1
                    cnt+=1
                    q.appendleft((nx,ny))
    return(cnt)

maeul = []
maeul_cnt = 0
for i in range(n):
    for j in range(n):
        if miro[i][j] == '1' and check[i][j]== 0:
            maeul.append(bfs(i,j))
            maeul_cnt +=1

maeul.sort()

print(maeul_cnt)
for i in maeul:
    print(i)

