import sys

shorties = [int(sys.stdin.readline().strip()) for _ in range(9)]

shorties.sort()

sum = -100

for shorty in shorties:
    sum += shorty

for i in range(9):
    for j in range(9):
        if shorties[i] + shorties[j] == sum:
            for k in range(9):
                if i != k and j != k:
                    print(shorties[k])
            
            exit()
           
                          