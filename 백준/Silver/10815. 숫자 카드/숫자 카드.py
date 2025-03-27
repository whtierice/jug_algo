import sys

N=int(sys.stdin.readline())
ist1=list(map(int,sys.stdin.readline().split()))
ist1.sort()

M=int(sys.stdin.readline())
ist2=list(map(int,sys.stdin.readline().split()))

ans=[]

for i in ist2:
    left=0
    right=N-1
    result=False

    while left<=right:
        mid=(left+right)//2

        if ist1[mid]<i:
            left=mid+1
        elif ist1[mid]>i:
            right=mid-1
        else:
            result=True
            break

    if result: 
                ans.append(1)
    else: 
        ans.append(0)

print(' '.join(map(str, ans)))