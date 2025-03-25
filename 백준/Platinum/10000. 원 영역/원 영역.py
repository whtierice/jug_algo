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

for i in range(n):
    x , r = list(map(int, sys.stdin.readline().split()))
    circles.append({'loc':x-r, 'brk':'('})
    circles.append({'loc':x+r, 'brk':')'})


circles.sort(key = lambda x : (x['loc'], -ord(x['brk'])))


# print(circles)

for i in range(n*2):
    loc= circles[i]['loc']
    brk= circles[i]['brk']

    if not stk:
        stk.append({'loc': loc, 'brk': brk, 'status': 0})
        continue

    if brk == ')':
        if stk [-1]['status'] == 1:
            ans += 2
        else:
            ans += 1
        stk.pop()
        # 만약 지금 완성되는 원과 맞닿는 원이 있다면, 스택에 가장 먼저들어온 괄호의 status 1로 유지, 아니라면 0으로 변경
        # 마지막 괄호는 어차피 접해있지 않으므로 확인 X
        if i != n*2 -1:
            if loc != circles[i+1]['loc']:
                stk[-1]['status'] = 0

    elif brk =='(':
        if stk[-1]['loc'] == loc:
            stk[-1]['status'] = 1
            stk.append({'loc': loc, 'brk': brk, 'status': 0})
        else:
            stk.append({'loc': loc, 'brk': brk, 'status': 0})


print(ans)













