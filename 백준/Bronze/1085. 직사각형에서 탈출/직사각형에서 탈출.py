import sys



a = list(map(int, sys.stdin.readline().split()))

b = a[0] - a[2]
c = a[1] - a[3]

if b < 0:
    b = b*-1

if c < 0:
    c = c*-1

if a[0] - a[1] > 0:
    d = a[1]
else:  
    d = a[0]

min = b

if min > c:
    min = c

if min > d:
    min = d

print(min)