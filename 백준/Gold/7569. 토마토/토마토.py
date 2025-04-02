import sys
from collections import deque

n, m, h = list(map(int,sys.stdin.readline().split()))

box = [ [ list(map(int, sys.stdin.readline().split())) for _ in range(m) ] for _ in range(h) ]

q = deque()

for z in range(h):
   for i in range(m):
       for j in range(n):
           if box[z][i][j] == 1:
               q.append((z,i,j))

di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while q:
   a, b, c = q.popleft()
   
   for i in range(6):
       nh = a + dz[i]
       ni = b + di[i]
       nj = c + dj[i]

       if 0 <= nh < h and 0 <= ni < m and 0 <= nj < n :
           if box[nh][ni][nj] == 0:
               box[nh][ni][nj] = box[a][b][c] + 1
               q.append((nh,ni,nj))

ans = 0

for z in range(h):
   for x in range(m):
       for y in range(n):
           if box[z][x][y] == 0:
               print(-1)
               exit(0)

           ans = max(ans, box[z][x][y])

print(ans-1)