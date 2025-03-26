import sys

n = int(sys.stdin.readline().strip())

li = list(map(int,sys.stdin.readline().split()))
li.sort()

left = 0
right = n-1
mini = abs(li[left] + li[right])

l_idx = left
r_idx = right

while left < right:
    summ = li[left] + li[right]
    

    if abs(summ) == 0:
        l_idx = left
        r_idx = right
        break

    if abs(summ) < mini:
        mini = abs(summ)
        l_idx = left
        r_idx = right
    
    if  summ > 0:
        right -=1
    elif summ < 0:
        left +=1
print(li[l_idx], li[r_idx])
