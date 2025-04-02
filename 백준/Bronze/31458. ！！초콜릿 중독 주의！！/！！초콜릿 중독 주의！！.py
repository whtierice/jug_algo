import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    idx = 0
    num = 0
    s = sys.stdin.readline().strip()
    for i in range(len(s)):
        if s[i] == '0' or s[i]== '1':
            idx = i
            num = int(s[i])
    
    for i in range(idx+1, len(s)):
        if s[i] == '!':
            num = 1
    
    for j in range(0, idx):
        if s[j] == '!':
            if num == 1:
                num = 0
            else:
                num = 1

    print(num)