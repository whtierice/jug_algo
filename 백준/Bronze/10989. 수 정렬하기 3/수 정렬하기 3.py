import sys

n = int(sys.stdin.readline().strip())

s_array = [0] * 10001

for i in range(n):
    s_array[int(sys.stdin.readline().strip())] += 1

for i in range(1,10001):
    if s_array[i] != 0:
        for _ in range(s_array[i]):
            print(i)
