import sys


n = int(sys.stdin.readline().strip())

s = []
for i in range(n):
    nn = int(sys.stdin.readline().strip())
    if nn != 0:
        s.append(nn)
    else:
        s.pop()
    

summ =sum(s)

print(summ)