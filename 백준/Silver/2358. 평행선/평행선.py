import sys

n = int(sys.stdin.readline().strip())

dictx = {}
dicty = {}

cnt = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    
    if a in dictx:
        dictx[a] += 1
    else:
        dictx[a] = 1
        
    if b in dicty:
        dicty[b] += 1
    else:
        dicty[b] = 1

for c in dictx:
    if dictx[c] >= 2:
        cnt +=1

for h in dicty:
    if dicty[h] >= 2:
        cnt+=1




print(cnt)