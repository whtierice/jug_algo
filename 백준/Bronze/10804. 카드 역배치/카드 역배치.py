import sys


def recur(a, pl,pr):
    if pl >= pr:
        return
    
    else:
        a[pl], a[pr] = a[pr], a[pl]
        
        recur(a,pl+1,pr-1)

a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(10):

    x, y = list(map(int,sys.stdin.readline().split()))
    recur(a,x-1,y-1)

for i in a:
    print(i, end=' ')
    
    