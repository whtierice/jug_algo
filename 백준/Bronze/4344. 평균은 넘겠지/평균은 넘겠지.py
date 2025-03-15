import sys

n = int(input())

for _ in range(n):
    total = 0
    count = 0
    reps = list(map(int, sys.stdin.readline().split()))

    nn = reps[0]
    score = reps[1:]

    for i in score:
        total += i

    average = total/nn

    for i in score:
        if i > average:
            count +=1

    print(f"{count / nn:.3%}")
