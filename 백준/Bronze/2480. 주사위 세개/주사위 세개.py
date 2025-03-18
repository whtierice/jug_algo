import sys

numbers = list(map(int,sys.stdin.readline().split()))

money = 0
max = numbers[0]



if numbers[0] == numbers[1] == numbers[2]:
    money = 10000 + (numbers[0] * 1000)
elif numbers[0] == numbers[1]:
    money = 1000 + (numbers[0] * 100)
elif numbers[0] == numbers[2]:
    money = 1000 + (numbers[0] * 100)
elif numbers[1] == numbers[2]:
    money = 1000 + (numbers[1] * 100)
else:
    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
    money = max * 100

print(money)

