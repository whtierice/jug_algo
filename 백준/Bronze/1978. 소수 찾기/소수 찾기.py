import sys

n = int(sys.stdin.readline())

numbers = list(map(int,sys.stdin.readline().split()))
cnt = 0

for number in numbers:
    if number < 2:
        continue

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    
    if is_prime:
        cnt +=1


print(cnt)

