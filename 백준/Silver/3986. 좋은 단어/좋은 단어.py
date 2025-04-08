import sys

n = int(sys.stdin.readline().strip())
cnt = 0

for _ in range(n):
    strr = sys.stdin.readline().strip()
    stk = []
    
    for str in strr:
        if not stk:
            stk.append(str)
        else:
            if stk[-1] == str:
                stk.pop()
            else:
                stk.append(str)
    
    if not stk:
        cnt+=1
    
    
print(cnt)