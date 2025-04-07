import sys

n = int(sys.stdin.readline().strip())

tt = []

for _ in range(n):
    a , b = list(map(int,sys.stdin.readline().split()))
    tt.append((a,b))

tt.sort(key = lambda x:(x[1], x[0]))

cnt = 1
e_time = 0

for s, e in tt:
    if e_time >0:
        if s >= e_time:
            cnt +=1
            e_time = e
    elif e_time == 0:
        e_time = e

print(cnt)

