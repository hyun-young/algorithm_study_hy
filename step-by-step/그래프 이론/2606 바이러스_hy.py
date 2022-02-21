"""
1번 컴퓨터와 연결된 모든 node 개수 출력

bfs : 32396kb 88ms
dfs : 32404kb 88ms
정답

bfs, dfs도 다익스트라 처럼 기본 틀에 익숙해지기!
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    # 1번 컴퓨터
    queue = deque([1])
    visited[1] = 1

    while queue:
        tmp = queue.popleft()
        for idx,v in enumerate(arr[tmp]):
            if not visited[idx] and idx != 0 and v:
                queue.append(idx)
                visited[idx] = 1
    print(visited)
    return sum(visited) - 1

def dfs(i):
    visited[i] = 1
    for idx,v in enumerate(arr[i]):
        if not visited[idx] and idx != 0 and v:
            dfs(idx)


n = int(input())
m = int(input())


arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1

#print(bfs())
dfs(1)
print(sum(visited) - 1)