import sys



def hanoi(n, x, y):

    if n == 1:
        print(x,y)
           
    else:
        hanoi(n-1, x, 6-x-y)
        print(x,y)
            
        hanoi(n-1,6-x-y,y)



racks = int(sys.stdin.readline().strip())

print(2**racks - 1)

if racks <21:
    hanoi(racks, 1, 3)