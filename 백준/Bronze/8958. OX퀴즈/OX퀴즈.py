import sys

n = int(input())

for _ in range(n):
    sum, score = 0, 0
    S = sys.stdin.readline().strip()

    for i in range(len(S)):
        if S[i] == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
