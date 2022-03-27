"""
2206 벽 부수고 이동하기와 유사문제
이동가능하면 1 불가능하면 0
"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(i,j):
    q = deque()
    q.append((i,j))
    arr[i][j] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1


dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
bfs(0,0)
#print(arr)
print(arr[-1][-1])
