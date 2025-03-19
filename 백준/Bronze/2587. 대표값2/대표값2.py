import sys

numbers = [int(sys.stdin.readline().strip()) for _ in range(5)]

for i in range(4):
    for j in range(4-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


sum = 0

for number in numbers:
    sum += number



print(int(sum / 5))
print(numbers[2])
