import sys

def ispal(s, l, r):
    if l >= r :
        return 1
    
    if s[l] != s[r]:
        return 0
    else:
        return ispal(s,l+1,r-1)


str = sys.stdin.readline().strip()

x = ispal(str, 0, len(str)-1)

print(x)

