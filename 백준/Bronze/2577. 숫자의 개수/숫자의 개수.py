import sys

A = int(input())
B = int(input())
C = int(input())

data = list(str(A * B * C))

for i in range(10):
    cnt = 0
    for da in data:
        if i == int(da):
            cnt += 1
    print(cnt)
