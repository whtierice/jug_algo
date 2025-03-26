import sys
import heapq
n = int(sys.stdin.readline().strip())
deck = [int(sys.stdin.readline().strip()) for _ in range(n)]

heapq.heapify(deck)
cnt = 0

while len(deck) > 1:
    temp = heapq.heappop(deck) + heapq.heappop(deck)
    cnt += temp

    heapq.heappush(deck, temp)

print(cnt)