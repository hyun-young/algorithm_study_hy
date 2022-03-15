"""
영역 개수 세기(빙산과 유사한 문제)
32428kb 1500ms 정답 (python 3)
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y,arr,visited,rain):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] - rain > 0 and not visited[nx][ny]: # 잠기지 않은지역이면서 방문 x 지역
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return

n = int(input())
arr = []
max_num = 1
min_num = 1e9

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    temp = list(map(int,input().split()))
    for each in temp:
        max_num = max(max_num,each)
        min_num = min(min_num,each)
    arr.append(temp)

if max_num == min_num:
    print(1)
    exit(0)

# 모두 다 잠기면 개수 0이라 판단 x
ans = 1
for rain in range(min_num,max_num):
    visited = [[0] * n for _ in range(n)]
    safety = 0 # 안전구역
    for i in range(n):
        for j in range(n):
            if arr[i][j] - rain > 0 and not visited[i][j]: # 현 위치가 빙산이면서 업데이트 안된 곳
                bfs(i,j,arr,visited,rain)
                safety += 1
    ans = max(ans,safety)

print(ans)
