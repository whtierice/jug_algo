import sys

n = int(sys.stdin.readline().strip())

score = 1
sum = 0

for i in range(n):

    
    score = 1
    sum = 0
    a = list(sys.stdin.readline().strip())

    for i in range(len(a)):
        if a[i] == 'O':
            if i > 0 and (a[i] == a[i-1]):
                score += 1
                sum += score
            else:
                sum += score
        else:
            score = 1

    
    print(sum)
