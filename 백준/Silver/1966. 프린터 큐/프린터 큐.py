import sys
from collections import deque

n = int(sys.stdin.readline().strip())


for _ in range(n):
    a , b = list(map(int,sys.stdin.readline().split()))

    # 우선순위
    w = list(map(int,sys.stdin.readline().split()))

    q = deque()
    cnt = 0
    for i in range(a):
        q.append((w[i],i))
    
    qq = b

    while q:
        if max(q)[0] == q[0][0]:
            if q[0][1] == b:
                q.popleft()
                cnt +=1
                break
            else:
                q.popleft()
                cnt +=1
        else:
            q.append(q.popleft())

    print(cnt)

    




    