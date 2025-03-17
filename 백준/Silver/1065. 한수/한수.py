import sys

x = int(sys.stdin.readline().strip())
cnt = 0

if x < 100:
    print(x)
else:
    cnt = 99

    for x in range(x,99, -1):
        x = str(x)
        
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])

        if (a-b) == (b-c):
            cnt +=1
            
        
        x = int(x)
    print(cnt)
    


