import sys


reps = int(input())

for _ in range(reps):
    r , s = sys.stdin.readline().split()
    for i in s:
        print(i * int(r), end="")
    print("")

