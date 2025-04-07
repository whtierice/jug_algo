import sys

n = int(sys.stdin.readline().strip())

tt = []

for _ in range(n):
    a , b = list(map(int,sys.stdin.readline().split()))
    tt.append((a,b))

tt.sort(key = lambda x:(x[1], x[0]))

result =[]

for s, e in tt:
    if result:
        if s >= result[-1][1]:
            result.append((s,e))
    else:
        result.append((s,e))

print(len(result))
