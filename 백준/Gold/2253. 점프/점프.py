import sys

n, m = list(map(int,sys.stdin.readline().split()))
falut = set()
stones = [i for i in range(1,n+1)]

for _ in range(m):
    falut.add(int(sys.stdin.readline().strip()))

dp = {i: {} for i in range(1,n+1)}

dp[1][0] = 0

for stone in stones:
    for pre_jump, jump_cnt in list(dp[stone].items()):
    # 현재에 대해 이전점프 -1, 이전점프, 이전점프+1 만큼 고려
        for next_jump in [pre_jump-1, pre_jump, pre_jump+1]:
            if next_jump <= 0:
                continue
            next_stone = stone + next_jump
            if next_stone in falut:
                continue
            if next_stone <= n and (next_jump not in dp[next_stone] or jump_cnt + 1 < dp[next_stone][next_jump]):
                dp[next_stone][next_jump] = jump_cnt + 1

if dp[n]:
    result = min(dp[n].values())
else:
    result = -1

print(result)

# print(dp)



