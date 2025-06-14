import sys
n, m = list(map(int,sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# print(n)
# print(m)
# print(a)
# print(b)
result = []

a_pointer = 0
b_pointer = 0

while a_pointer < n and b_pointer < m:
    #print(f"b_pointer : {b_pointer}")
    if a[a_pointer] > b[b_pointer]:
        result.append(b[b_pointer])
        #print(f"a_pointer : {a_pointer}")
        #print(f"b_pointer : {b_pointer}")
        b_pointer +=1
    else:
        result.append(a[a_pointer])
        a_pointer +=1
# print(*result)
# print(len(a))
# print(len(b))
# print(f"a_pointer : {a_pointer}")
# print(f"b_pointer : {b_pointer}")

if a_pointer == n:
    while b_pointer < m:
        #print(f"len of b: {len(b)}")
        result.append(b[b_pointer])
        b_pointer +=1
elif b_pointer == m:
    while a_pointer < n:
        #print(f"len of a: {len(a)}")
        result.append(a[a_pointer])
        a_pointer +=1

print(*result)