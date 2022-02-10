"""
bfs인데, 지점간의 거리를 구하고 거리가 최대일 때를 구할 수있나?
모든 지점에서 최대 거리를 구하는 완전탐색(조건이 50*50이기 때문(hint))
출처 : https://resilient-923.tistory.com/291
"""

import sys
from collections import deque

input = sys.stdin.readline

a,b = map(int,input().split())

graph = []
for _ in range(a):
    graph.append(list(input().rstrip()))

# 방향좌표
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,cnt):
    # 한 지점에서 bfs를 둘 때 현재 cnt값이 최대인지 아닌지 구분
    max_cnt = -1
    q = deque()
    q.append(((x,y,cnt)))
    visited[x][y] = 1 # 첫 queue(1이면 방문)

    while q:
        x,y,cur_cnt = q.popleft()
        if max_cnt < cur_cnt:
            max_cnt = cur_cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < a and 0 <= ny < b and graph[nx][ny] == 'L' and not visited[nx][ny]:
                q.append((nx, ny, cur_cnt + 1))
                visited[nx][ny] = 1
    return max_cnt

ans = -1
for i in range(a):
    for j in range(b):
        if graph[i][j] == 'L':
            # l일때만 queue에 넣기
            # visited 계속 0으로 초기화 진행행
            visited = [[0]*b for _ in range(a)]
            ans = max(ans,bfs(i,j,0))

print(ans)