import sys 
import heapq

n = int(sys.stdin.readline().strip())



for i in range(n):
    
    q = int(sys.stdin.readline().strip())
    ans = []
    leftheap = []
    rightheap = []
    for i in range(q//10 + 1):
        num = list(map(int, sys.stdin.readline().split()))
        
        for k in range(len(num)):
            ls = len(leftheap)
            rs = len(rightheap)
            if ls > rs:
                heapq.heappush(rightheap, num[k])
            else:
                heapq.heappush(leftheap, -num[k])
            
            if rightheap and -leftheap[0] > rightheap[0]:
                leftValue = heapq.heappop(leftheap)
                rightValue = heapq.heappop(rightheap)

                heapq.heappush(leftheap, -rightValue)
                heapq.heappush(rightheap, -leftValue)
        
            if (k+1) % 2 == 1:
                ans.append(-leftheap[0])
        
        if i +1 == q//10 +1:
            print(len(ans))
            for l in range(0, len(ans), 10) :
                print(*ans[l:min(l+10, len(ans))])

                


