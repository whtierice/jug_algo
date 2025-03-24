import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

k = int(input())
apple = deque()
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))

l = int(input())
dq = deque()
for _ in range(l):
    a, b = input().split()
    a = int(a)
    dq.append((a, b))

bam = deque()
time = 0
x, y = 1, 1
direction = 0 # 0우 1상 2좌 3하
bam.append((x, y))

while True:
    time += 1
    
    # 뱀 이동
    if direction == 0:
        y += 1
    elif direction == 1:
        x -= 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x += 1

    # 벽에 부딪히면 게임 오버
    if x < 1 or x > n or y < 1 or y > n:
        #print("GAME OVER: 벽에 부딪혔습니다")
        break

    # 자기 자신한테 부딪히면 게임 오버
    if (x, y) in bam:
        #print("GAME OVER: 스스로 부딪혔습니다")
        break

    bam.append((x, y))
    # 사과를 먹으면 머리만 늘어남
    if (x, y) in apple:
        apple.remove((x, y))
    else:
        bam.popleft()
        
    # 방향 전환
    if (time, 'L') in dq or (time, 'D') in dq:
        d = dq.popleft()
        if d[1] == 'D': # 왼쪽으로 90도 회전
            direction -= 1
            if direction == -1:
                direction = 3
        else: # 오른쪽으로 90도 회전
            direction += 1
            if direction == 4:
                direction = 0
    
print(time)