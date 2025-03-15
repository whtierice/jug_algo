import sys

words = sys.stdin.readline().split()
count = 0

for word in words:
    count +=1

print(count)