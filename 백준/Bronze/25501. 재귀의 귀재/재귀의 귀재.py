import sys

reps = int(sys.stdin.readline().strip())

cnt = 0

def recur(s, l, r):
    global cnt
    
    cnt += 1
    if l >= r:
        return 1 , cnt
    
    if s[l] != s[r]:
        return 0, cnt
    else:
        return recur(s,l+1,r-1)

    

def ispal(s):
    return recur(s,0,len(s)-1)



for _ in range(reps):
    str = list(sys.stdin.readline().strip())
    a , b = ispal(str)
    print(a,b)
    cnt = 0

