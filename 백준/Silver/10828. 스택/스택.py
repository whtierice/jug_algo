import sys

reps = int(sys.stdin.readline().strip())


s = []



for i in range(reps):
    comm = list(sys.stdin.readline().split())
    if len(comm) == 2:
        comm[1] = int(comm[1])

    if comm[0] == 'push':
        s.append(comm[1])
    elif comm[0] == 'pop':
        if not s:
            print(-1)
        else:
            print(s.pop())
    elif comm[0] == 'size':
        print(len(s))
    elif comm[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif comm[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)

    
