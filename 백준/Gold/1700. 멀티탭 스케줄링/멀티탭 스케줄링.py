import sys
from collections import deque

n, k = list(map(int,sys.stdin.readline().split()))

order = deque(list(map(int,sys.stdin.readline().split())))

mult = []
cnt = 0

while order:
    cur = order.popleft()

    if cur in mult:
        continue

    if len(mult) < n:
        mult.append(cur)
        continue

    outt = None

    for dev in mult:
        if dev not in order:
            outt = dev
            break

    if outt is None:
        mx_idx = -1
        for devv in mult:
            cur_idx = order.index(devv)
            if cur_idx > mx_idx:
                mx_idx = cur_idx
        
        outt = order[mx_idx]
    
    
    mult.remove(outt)
    mult.append(cur)
    cnt +=1

    

print(cnt)



