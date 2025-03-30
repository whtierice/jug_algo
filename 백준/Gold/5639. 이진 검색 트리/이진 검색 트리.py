import sys
sys.setrecursionlimit(10**6)

# 1단계: 전위 순회 배열의 첫 값이 루트임
# 2단계: 루트보다 작은 값은 왼쪽 서브트리, 루트보다 큰 값은 오른쪽 서브트리로 구분
# 3단계: 좌우 서브트리에 대해 재귀적으로 같은 과정을 수행한 후, 후위 순회 순서대로 노드를 출력.

# 전위 순회 결과를 저장할 리스트
preorder = []

# 입력을 모두 읽어 int형으로 변환하여 리스트에 저장
for line in sys.stdin:
    line = line.strip()
    if line:
        preorder.append(int(line))


def solve(start, end):
    if start >= end:
        return
    
    root = preorder[start]
    idx = start + 1

    while idx < end and root > preorder[idx]:
        idx +=1

    solve(start + 1, idx)
    solve(idx , end)
    print(root)
    

solve(0, len(preorder))
