import sys
from collections import deque
n, m = list(map(int,sys.stdin.readline().split()))

a = deque(list(map(int, sys.stdin.readline().split())))
b = deque(list(map(int, sys.stdin.readline().split())))

# print(n)
# print(m)
# print(a)
# print(b)
result = []

a_pointer = 0
b_pointer = 0

while a and b:
    #print(f"b_pointer : {b_pointer}")
    if a[0] > b[0]:
        result.append(b.popleft())
        #print(f"a_pointer : {a_pointer}")
        #print(f"b_pointer : {b_pointer}")
        #b_pointer +=1
    else:
        result.append(a.popleft())
        a_pointer +=1
# print(*result)
# print(len(a))
# print(len(b))
# print(f"a_pointer : {a_pointer}")
# print(f"b_pointer : {b_pointer}")

if not a:
    while b:
        #print(f"len of b: {len(b)}")
        result.append(b.popleft())
elif not b:
    while a:
        #print(f"len of a: {len(a)}")
        result.append(a.popleft())

print(*result)