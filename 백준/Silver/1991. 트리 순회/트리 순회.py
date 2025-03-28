import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def 전위순회(root):
    if root is None:
        return
    
    print(root.val, end='')
    전위순회(root.left)
    전위순회(root.right)

def 중위순회(root):
    if root is None:
        return
    
    중위순회(root.left)
    print(root.val, end='')
    중위순회(root.right)

def 후위순회(root):
    if root is None:
        return
    후위순회(root.left)
    후위순회(root.right)
    print(root.val, end = '')

n = int(sys.stdin.readline().strip())
# key 값이 부모, value는 튜플로 각각 (왼쪽 자식, 오른쪽 자식)
nodes ={}

for _ in range(n):
    pa, l, r = sys.stdin.readline().split()
    
    if pa not in nodes:
        nodes[pa] = Node(pa)
    
    if l != '.':
        if l not in nodes:
            nodes[l] = Node(l)
        nodes[pa].left = nodes[l]
    
    if r != '.':
        if r not in nodes:
            nodes[r] = Node(r)
        nodes[pa].right = nodes[r]


root = nodes['A']

전위순회(root)
print()
중위순회(root)
print()
후위순회(root)







