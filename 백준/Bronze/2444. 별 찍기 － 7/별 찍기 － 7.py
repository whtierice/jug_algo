import sys

n = int(sys.stdin.readline().strip())


def recur_star(n, cnt):
    if cnt +1 == n:
        print("*", end='')
        print("**" * cnt, end='')
        print()
        return
    
    print(' ' * (n-cnt-1), end='')
    print("*", end='')
    print("**" * cnt, end='')
    print()

    recur_star(n, cnt+1)

    print(' ' * (n-cnt-1), end='')
    print("*", end='')
    print("**" * cnt, end='')
    print()

recur_star(n,0)