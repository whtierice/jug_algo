# 재귀로 구현
# O(2^n)
d = [0] * 1000

def dp(x):
	if (x==1):
		return 1
	if (x==2):
		return 1
		
	return dp(x-1) + dp(x-2)
	

# DP로 구현
# O(n)

def dpp(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = dpp(x-1) + dpp(x-2)
    return d[x]



x = int(input())
print(dpp(x))