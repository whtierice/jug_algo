import sys

n, m =list(map(int,sys.stdin.readline().split()))
firewood = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(firewood)

while left <= right:
    mid = (left + right) // 2
    
    sum = 0
    for i in firewood:
        if i >= mid:
            sum += i - mid

    
    if sum >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)