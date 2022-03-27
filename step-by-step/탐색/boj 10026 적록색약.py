"""
적록색약 (빨강-초록 합쳐서 보기)
bfs case 2개, arr값 변경해서 bfs함수 2번 사용하는 방식으로!
32452kb 128ms 정답
"""

import sys
from collections import deque

input = sys.stdin.readline

# 동서남북
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,color):
    q = deque()
    q.append(((x,y)))
    visited[x][y] = 1 # 첫 queue(1이면 방문)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]==color and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

def solution(arr,visited):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = arr[i][j]
                bfs(i,j,color)
                cnt += 1
    return cnt


n = int(input())
arr = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(input().strip()))

# case 1 정상인
print(solution(arr,visited), end=' ')

# case 2 적록색약
visited = [[0]*n for _ in range(n)] # 전역변수 초기화!
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R': # arr 색깔 변경
            arr[i][j] = 'G'

print(solution(arr,visited))



