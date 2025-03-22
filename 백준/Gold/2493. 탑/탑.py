import sys


N = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))

ans = [0] * N
stk = []

for i in range(N):
    while stk:
        if top[i] > stk[-1][1]:
            stk.pop()
        else:
            ans[i] = stk[-1][0]
            break
    
    stk.append((i+1,top[i]))

print(*ans)

    
            
        
    