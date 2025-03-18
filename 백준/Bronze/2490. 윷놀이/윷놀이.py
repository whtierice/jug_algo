import sys

for i in range(3):
    cnt = 0
    yy = list(map(int, sys.stdin.readline().split()))

    for j in yy:
        if j == 1:
            cnt +=1
    
    if cnt == 0:
        print("D")
    elif cnt == 1:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("A")
    else:
        print("E")