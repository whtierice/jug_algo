from collections import defaultdict

def p_path(points, route):
    tuple_points = [0] + [tuple(point) for point in points]
    r, c = tuple_points[route[0]] # 시작점
    t = 0
    
    path = []
    path.append((t,r,c))
    for i in range(len(route) - 1):
        r2,c2 = tuple_points[route[i+1]]

        while r != r2:
            if r2 > r:
                r +=1
            else:
                r -= 1

            t += 1

            path.append((t,r,c))

        while c != c2:
            if c2 > c:
                c +=1
            else:
                c -=1
            t+=1
            path. append((t,r,c))


    return path

def solution(points, routes):
    cnt = defaultdict(int)
    for route in routes:
        for p in p_path(points, route):
            cnt[p] += 1
            
    answer = 0
    
    for value in cnt.values():
        if value >= 2:
            answer +=1
    
    return answer

    
        
        