import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
queue = deque()
result = []

for i in range(1,N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<",end ='')
for j in range(N-1): 
    print('%d, '%result[j],end='')
print(result[-1],end='')
print(">")
