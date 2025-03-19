import sys

numbers = [i for i in range(1,1001)]



a, b = (list(map(int,sys.stdin.readline().split())))




if b > a:
    print(b-a-1)

    for i in range(a, b-1):
        if i == b-2:
            print(numbers[i])
        else:
            print(f"{numbers[i]} ", end='')
elif a > b:
    print(a-b-1)

    for i in range(b, a-1):
        if i == a-2:
            print(numbers[i])
        else:
            print(f"{numbers[i]} ", end='')
else:
    print(0)