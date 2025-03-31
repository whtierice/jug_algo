import sys

n = int(sys.stdin.readline().strip())


pivot = list(sys.stdin.readline().strip())

for i in range(n-1):
    comp = list(sys.stdin.readline().strip())

    for j in range(len(comp)):
        if comp[j] != pivot[j]:
            pivot[j] = '?'

for k in range(len(pivot)):

    print(pivot[k], end ='')