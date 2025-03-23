import sys 
import heapq

n = int(sys.stdin.readline().strip())

lefthip = []
righthip = []
ans = []

for i in range(n):
    num = int(sys.stdin.readline().strip())
    lhl = len(lefthip)
    rhl = len(righthip)

    if lhl > rhl:
        heapq.heappush(righthip,num)
    else:
        heapq.heappush(lefthip,-num)
    
    if righthip and -(lefthip[0]) > righthip[0]:
        leftValue = heapq.heappop(lefthip)
        rightValue = heapq.heappop(righthip)

        heapq.heappush(lefthip, -rightValue)
        heapq.heappush(righthip, -leftValue)

    ans.append(-lefthip[0])

for a in ans:
    print(a)


