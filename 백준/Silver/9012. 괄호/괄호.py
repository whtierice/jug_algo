import sys

reps = int(sys.stdin.readline().strip())

for i in range(reps):
    strr = sys.stdin.readline().strip()
    stack = []
    status = True
    for char in strr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                status = False
                break
    if status and not stack:
        print('YES')
    else:
        print('NO')
    