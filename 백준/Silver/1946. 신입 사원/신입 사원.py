import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    applicant = []
    for _ in range(n):
        a, b = list(map(int,sys.stdin.readline().split()))
        applicant.append((a,b))
    result = []

    applicant.sort()


    for re, it in applicant:
        if not result:
            result.append(applicant[0])
            continue

        if re < result[-1][0] or it < result[-1][1]:
            result.append((re,it))
        

    print(len(result))





    