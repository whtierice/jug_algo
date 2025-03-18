import sys

line = int(sys.stdin.readline().strip())

for i in range(line):
    for j in range(line):
        if i + j >= line:
            print("", end='')
        else:
            print("*", end='')
    print("")