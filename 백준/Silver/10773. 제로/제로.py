import sys


n = int(sys.stdin.readline().strip())

s = []
for i in range(n):
    m = int(sys.stdin.readline().strip())
    if m != 0:
        s.append(m)
    else:
        s.pop()

sum = 0

for t in s:
    sum+=t

print(sum)