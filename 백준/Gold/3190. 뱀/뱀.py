import sys
input = sys.stdin.readline
from collections import deque

apple = deque()
snake = deque()
dir_ch = deque()
dir = 1
time = 0

n = int(input())


k = int(input())


(x,y) = (1,1)
snake.append((x,y))

for _ in range(k):
    a , b = list(map(int,input().split()))
    apple.append((a,b))

# apple = [(3,4), (2,5), (5,3)]

l = int(input())

for _ in range(l):
    a , b = list((input().split()))
    a = int(a)
    dir_ch.append((a,b))

#dir_ch = [(3,D), [(15,L), (17,D)]




while True:
    time +=1

    
    # 이동
    if dir ==1:
        y +=1
    
    if dir == 0:
        x -=1

    if dir == 2:
        x+=1

    if dir ==3:
        y-=1

    # 경기장 밖을 나간 경우
    if x > n or  y > n or x < 1 or y < 1 :
        break
    
    # 자기 몸에 부딪힌 경우
    if (x,y) in snake:
        break
    
    # 사과를 안먹은 경우 길이변화x
    if (x,y) not in apple:
        snake.append((x,y))
        snake.popleft()
    else:
        snake.append((x,y))
        apple.remove((x,y))
        
    
    # 방향변화 시간이 된 경우
    if (time, 'L') in dir_ch or (time, 'D') in dir_ch:
        d = dir_ch.popleft()
        if d[1] == 'L':
            if dir == 0:
                dir = 3
            else:
                dir -=1
        
        if d[1] == 'D':
            if dir == 3:
                dir = 0
            else:
                dir +=1
        

print(time)


