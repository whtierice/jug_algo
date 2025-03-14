import sys

number = int(input())

for _ in range(number):
    a , b = list(map(int,sys.stdin.readline().split()))
    print(a+b)
