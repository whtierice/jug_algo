n, m = map(int, input().split())
field = []
for _ in range(m):
    field.append(list(input().strip()))

visited = [[False] * n for _ in range(m)]

def dfs(x, y, color):
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    
    # 이미 방문했거나 적이면 나가기
    if visited[x][y] or field[x][y] != color:
        return 0
    
    visited[x][y] = True
    count = 1
    
    # 4방향 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        count += dfs(x + dx, y + dy, color)
    
    return count


### 메인

white_power = 0
blue_power = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            color = field[i][j]
            area_size = dfs(i, j, color)
            
            if color == 'W':
                white_power += area_size ** 2
            elif color == 'B':
                blue_power += area_size ** 2

print(white_power, blue_power)