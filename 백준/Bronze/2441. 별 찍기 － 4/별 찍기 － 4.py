import sys

line = int(sys.stdin.readline().strip())

for i in range(line):
    print(' ' * i,end ='')
    print("*" * (line - i), end='')
    print('')