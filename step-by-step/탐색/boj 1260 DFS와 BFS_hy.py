"""
너비우선탐색으로 선입선출 queue를 이용해 맨앞으로 뽑힌 노드와 연결되는 같은 너비 노드 선을 먼저 탐색
깊이우선탐색으로 재귀 이용해 맨 마지막에 뽑힌 노드와 연결되는 깊이 우선인 선을 먼저 탐색
bfs : queue, dfs: recursion

주의: 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다

38268kb, 256ms 정답
"""

import sys
from collections import deque

input = sys.stdin.readline

def dfs(root):
    #재귀 및 출력부분 고민
    visited_dfs[root] = 1
    print(root, end=' ')
    for idx,v in enumerate(edge[root]):
        if not visited_dfs[idx] and idx != 0 and v:
            dfs(idx)


def bfs(root):
    q = deque([root])
    visited_bfs[root] = 1
    ans = []
    while q:
        tmp = q.popleft()
        ans.append(tmp)
        for idx,v in enumerate(edge[tmp]):
            if not visited_bfs[idx] and idx != 0 and v:
                q.append(idx)
                visited_bfs[idx] = 1
    print(*ans)
    return


n,m,root = map(int,input().split())

edge = [[0]*(n+1) for _ in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
result = []
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향
    edge[a][b] = 1
    edge[b][a] = 1

dfs(root)
print()
bfs(root)
