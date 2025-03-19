import sys

reps = int(sys.stdin.readline().strip())

for i in range(reps-1,-1,-1):
    print(' '*(reps-1-i), end='')
    print('*'*(2*i), end='')
    print('*', end='')
    print()
