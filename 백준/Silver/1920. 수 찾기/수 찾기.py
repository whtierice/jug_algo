import sys

n = int(sys.stdin.readline().strip())

l1 = list(map(int,sys.stdin.readline().split()))
l1.sort()

m = int(sys.stdin.readline().strip())

l2 = list(map(int,sys.stdin.readline().split()))


for i in range(len(l2)):
    ans = 0
    start = 0
    end = len(l1)-1

    while start <= end:
        mid = (start+end) // 2 
        
        if l2[i] == l1[mid]:
            ans = 1
            break
        elif l2[i] > l1[mid]:
            start = mid +1
        elif l2[i] < l1[mid]:
            end = mid -1
    
    print(ans)
        

    