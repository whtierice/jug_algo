import sys

x , y = list(map(int,sys.stdin.readline().split()))

hr = [0 , x]
vt = [0 , y]


reps = int(sys.stdin.readline().strip())

for i in range(reps):
    a , b = list(map(int,sys.stdin.readline().split()))

    if a == 0:
        vt.append(b)
    else:
        hr.append(b)

hr = sorted(hr)
vt = sorted(vt)

hr_max = 0
vt_max = 0

for i in range(len(hr)-1,0, -1):
    if hr[i] - hr[i-1] > hr_max:
        hr_max = hr[i] - hr[i-1]

for i in range(len(vt)-1,0, -1):
    if vt[i] - vt[i-1] > vt_max:
        vt_max = vt[i] - vt[i-1]


print(hr_max * vt_max)
