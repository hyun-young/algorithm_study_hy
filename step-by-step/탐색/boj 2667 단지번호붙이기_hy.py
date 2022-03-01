"""
연결된 집: 단지(상하좌우 연결)

총 단지수, 각 단지에 속하는 집의 수를 오름차순으로 출력

34516kb 96ms 정답
"""

import sys
import heapq
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append(((x,y)))
    visited[x][y] = 1 # 첫 queue(1이면 방문)
    cnt = 0
    while q:
        x,y = q.popleft()
        arr[x][y] = 0 # 한번 cnt한 곳은 0으로 반드시 초기화해야 또 queue에 안 넣음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    for row in visited:
        cnt += sum(row)
    return cnt


n = int(input())
arr = [[] for _ in range(n)]
ans = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    arr[i] = list(map(int,input().rstrip()))

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            # 1일때만 queue에 넣기(이미 센 곳은 함수에서 0으로 초기화)
            # visited 계속 0으로 초기화 진행행
            visited = [[0]*n for _ in range(n)]
            heapq.heappush(ans,(bfs(i,j)))

print(len(ans))
# 최솟값 뽑아내기, heap과 sort 큰 차이 없었음
for _ in range(len(ans)):
    print(heapq.heappop(ans))
