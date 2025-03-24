import sys

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def check색종이(N, x, y):
    global maps
    sum = 0
    for i in range(y, y+N):
        for j in range(x, x+N):
            sum += maps[i][j]

    if sum == 0:
        return 0
    elif sum == N * N:
        return 1
    else:
        return -1

def 색종이(N, x, y):
    global white, blue, maps
    check = check색종이(N, x, y)

    if check == 1:
        blue += 1
        return
    elif check == 0:
        white += 1
        return

    half = N // 2
    # if x < half and y < half:
    색종이(half, x, y)
    # if x + half >= half > y:
    색종이(half, x + half, y)
    # if x < half <= y + half:
    색종이(half, x, y + half)
    # if x + half >= half and y + half >= half:
    색종이(half, x + half, y + half)

색종이(N, 0, 0)


print(white)
print(blue)

