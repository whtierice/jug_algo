import sys


n = int(sys.stdin.readline().strip())

m = [int(sys.stdin.readline().strip()) for _ in range(n)]

b = m[-1]

cnt = 1

for mm in reversed(m):
    if b < mm:
        b = mm
        cnt+=1

print(cnt)