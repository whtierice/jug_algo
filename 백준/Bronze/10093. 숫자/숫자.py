import sys

a, b = (list(map(int,sys.stdin.readline().split())))


if b > a:
    print(b-a-1)
    for i in range(a+1, b):
        print(i, end=' ')


elif a > b:
    print(a-b-1)
    for i in range(b+1, a):
        print(i, end=' ')

else:
    print(0)