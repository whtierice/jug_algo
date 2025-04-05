import sys

n, m = list(map(int, sys.stdin.readline().split()))

mo = []
cnt = 0
for i in range(n):
    mo.append(int(sys.stdin.readline().strip()))

mo.sort(reverse=True)

for i in range(n):
    if mo[i] <= m:
        cnt += m // mo[i]
        m = m % mo[i]


print(cnt)