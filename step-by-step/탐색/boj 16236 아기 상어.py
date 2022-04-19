"""
지나갈 수 있는 것: 자신의 크기보다 작거나 같음
먹을 수 있는 것 : 자신의 크기보다 작음
상어 크기는 자신의 크기만큼 물고기를 먹어야 +1
"""
import sys
from collections import deque
import heapq

input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    heap = []
    q.append((x,y,0))

    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0 or size == arr[nx][ny]: # 지나갈 수 있는 곳 q에 저장
                    q.append((nx,ny,dist+1))
                elif size > arr[nx][ny]: #먹을 수 있는 곳은 heap에 저장
                    heapq.heappush(heap,(dist+1,nx,ny))
    print('arr ', arr)
    print(heap)
    if heap:
        return heapq.heappop(heap) # 가장 적게 걸리는 것 반환
    else:
        return None

dx=[-1,1,0,0]
dy=[0,0,1,-1]

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
size = 2
time = 0
eaten = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0 # 지나갈 수 있는 곳으로 바꾸기 위해 0으로 변경
            cx,cy = i,j

while 1:
    visited = [[0] * n for _ in range(n)]
    visited[cx][cy] = 1
    result = bfs(cx,cy)

    if result == None:
        break
    cx, cy = result[1], result[2]
    eaten += 1
    time += result[0]
    arr[cx][cy] = 0 # 현재 있는 곳

    if eaten == size:
        eaten = 0 # 먹은 물고기 초기화
        size += 1

print(time)