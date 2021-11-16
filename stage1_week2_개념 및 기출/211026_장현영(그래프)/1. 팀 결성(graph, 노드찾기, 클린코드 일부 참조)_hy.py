import sys

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 재귀적으로 부모노드 갱신
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    team, a, b = map(int, input().split())
    if team == 0:  # 팀을 합치는 연산
        union_parent(parent, a, b)
    else:  # 팀 찾기 연산
        root_a = find_parent(parent, a)
        root_b = find_parent(parent, b)
        if root_a == root_b: # 부모노드 같으면 같은팀
            print('YES')
        else:
            print('NO')
