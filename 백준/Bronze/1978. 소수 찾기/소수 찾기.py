import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0

for num in numbers:
    if num == 2:
        cnt +=1
        continue
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num -1:
                cnt+=1    

print(cnt)