import sys


numbers = [int(sys.stdin.readline().strip()) for i in range(7)]

sum = 0
mini = 1000



for number in numbers:
    if number % 2 == 1:
        sum += number
        if number < mini:
            mini = number

if sum == 0:
    print(-1)
else:
    print(sum)
    print(mini)




