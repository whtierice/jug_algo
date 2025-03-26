import sys

n , c = list(map(int,sys.stdin.readline().split()))

hp = [int(sys.stdin.readline().strip()) for _ in range(n)]

hp.sort()

min = 1
max = hp[-1] - hp[0]

ans = 0

while min <= max:
    mid = (min + max) // 2
    ch = hp[0]
    cnt = 1
    
    for i in range(1,n):
        if hp[i] >= mid + ch:
            cnt +=1
            ch = hp[i]

    if cnt >= c:
        min = mid+1
        ans = mid
    else:
        max = mid - 1

print(ans)