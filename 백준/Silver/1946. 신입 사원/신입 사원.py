import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    m = int(sys.stdin.readline().strip())
    content = []
    for i in range(m):
        a, b = list(map(int,sys.stdin.readline().split()))
        content.append((a,b))

    content.sort()
    result = []
    for m, s in content:
        if result:
            if m <= result[-1][0] or s <= result[-1][1]:
                result.append((m,s))
        else:
            result.append((content[0][0], content[0][1]))
        
    print(len(result))