import sys

def is_prime_num(n):
	for i in range(2, n):
		if n % i == 0:
			return False
		
	return True
            

reps = int(sys.stdin.readline().strip())



for _ in range(reps):

    num = int(sys.stdin.readline().strip())
	
    a = num // 2
    b = num // 2
	
    for _ in range(num):
        if is_prime_num(a) and is_prime_num(b):
            break
        else:
            a -= 1
            b += 1
    
    print (a, b)
		