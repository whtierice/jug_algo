import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

# 각 학생(노드)에서 다음 학생들(노드)로의 연결 정보를 저장 (1번부터 N번까지 사용)
st = [[] for _ in range(N+1)]

# 각 학생의 진입 차수를 저장 (몇 개의 학생이 자신보다 먼저 와야 하는지)

od = [0] * (N+1)

# M개의 비교 정보를 입력받아 그래프와 진입 차수 갱신
for i in range(M):
    a , b = map(int,input().split())
    st[a].append(b)
    od[b] +=1



q = deque()

# 진입 차수가 0인 학생(아무도 자신보다 먼저 올 필요가 없는 학생)을 큐에 추가
for i in range(1,N+1):
    if od[i] == 0:
        q.append(i)

result = []
# 위상 정렬 수행
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in st[cur]:
        od[nxt] -= 1  # cur 학생을 처리했으므로, nxt 학생의 진입 차수를 1 감소
        if od[nxt] == 0:
            q.append(nxt)



# 결과 출력: 학생 번호들을 공백으로 구분하여 출력
print(*result)


