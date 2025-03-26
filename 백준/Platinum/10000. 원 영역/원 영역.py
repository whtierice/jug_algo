# pseudo code

# 원의 시작점과 반지름을 이용하여 왼쪽은 '(' 오른쪽은 ')'로 만든다
# 좌표를 기준으로 오름차순 정렬, 좌표가 같다면 ')'이 오도록 설정
# 스택에는 좌표, 좌우, 접선 여부를 확인하는 상태값이 들어간다
# 스택에 아무것도 없으면 지금 값을 넣고 다음 루프로
# 지금 루프의 좌우가 ')'라면,
# 지금 스택에 있는 원에 대하여 status가 0이면 답에 1증가 1이면 답에 2증가
# 증가한 뒤 pop
# 만약 이어지는 원이 있다면, status 1로 유지, 아니라면 0으로 변경
# 지금 루프의 좌우가 '('라면, 
# 지금 스택에 있는 최신 자료와 좌표가 같을 경우, 그 자료의 상태값 1로변경하고 지금 루프 스택에 올리기
# 아니라면 원이 접하지 않으므로 status를 0으로 하고 스택에 추가

import sys


n = int(sys.stdin.readline().strip())
circles = []
stk = []
ans = 1

for _ in range(n):
    x , r = list(map(int,sys.stdin.readline().split()))
    circles.append((x-r, "("))
    circles.append((x+r, ")"))

circles.sort(key = lambda x: (x[0], -ord(x[1])))



for i in range(n*2):
    if not stk:
        stk.append({'pos': circles[i][0], 'brk': circles[i][1], 'status': 0})
    

    if circles[i][1] == '(':
        if stk[-1]['pos'] == circles[i][0]:
            stk[-1]['status'] = 1
            stk.append({'pos': circles[i][0], 'brk': circles[i][1], 'status': 0})
        else:
            stk.append({'pos': circles[i][0], 'brk': circles[i][1], 'status': 0})
    else:
        if stk[-1]['status'] == 0:
            ans +=1
        else:
            ans +=2 
        
        stk.pop()
        
        if i != 2*n-1:
            if circles[i][0] != circles[i+1][0]:
                stk[-1]['status'] = 0









    

print(ans)


