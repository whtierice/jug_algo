import sys

reps = int(sys.stdin.readline().strip())

for i in range(reps):
    print(' '*(reps-1-i), end='')
    print('*', end='')
    print('*'*(2*i), end='')
    print()

