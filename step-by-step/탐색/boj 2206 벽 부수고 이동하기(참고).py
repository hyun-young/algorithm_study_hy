"""
이동 중 한번만 벽 부수기 가능!
n,m --> 1000까지라서 모든 경우 계산 불가능
2178 미로탐색 유사문제
이동가능하면 0 불가능하면 1
https://seongonion.tistory.com/m/107
"""

import sys
from collections import deque

input = sys.stdin.readline

# z = 0(벽 안 뚫음)
# z = 1 (길이 막혔을 때 벽을 한번 뚫어서 이동해보기)
def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    visited[x][y][z] = 1
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 이동이 가능하고, 아직 방문하지 않은 곳이라면
                if not arr[nx][ny] and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
                # 이동이 불가능한 경우에 벽을 아직 부순 적 없다면 (딱 한번 이하로 사용되는 곳)
                # 해당하는 즉시 z=1에서만 기록됨
                if arr[nx][ny] and z == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1 # z=0일때 값 + 1 가져가기
                    q.append((nx,ny,z+1))
    return -1


dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs(0,0,0))