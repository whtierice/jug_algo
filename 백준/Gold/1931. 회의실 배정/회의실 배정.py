import sys

n = int(sys.stdin.readline().strip())

tt = []

for _ in range(n):
    a , b = list(map(int,sys.stdin.readline().split()))
    tt.append((b,a))

tt.sort()

result = []


for end, start in tt:
    if not result:
        result.append((start,end))
        continue

    if start >= result[-1][1]:
        result.append((start,end))

print(len(result))


