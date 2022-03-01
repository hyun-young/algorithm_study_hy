"""
1 : 익은 토마토
0 : 안 익은 토마토(target)
-1 : 토마토가 없는 곳(벽)

기존 풀이와 다르게 visited를 쓰지 않고 arr에 토마토 익은 날짜를 update해주는 방식으로
(3차원 메모리 문제)

if문 쓸 때 값이 1,0일때만 조건으로 등호빼고 쓰기 (-1도 if에 인식됨)

47788kb 3164ms 정답

"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            # 1인 영역이 있는 곳에 0이 있다면 날짜 세어주기
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny]==0:
                arr[nz][nx][ny] = arr[z][x][y] + 1 # 기존 1에서 1씩 더해나가기
                q.append((nz,nx,ny))

# h층 n행 m열
m,n,h = map(int,input().split())
arr = []

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

# arr list 받기
for k in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)

# 익은 토마토 q에 넣고 한번에 돌려주기 (visited 사용 x arr 업그레이드 할 예정)
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1: # 틀렸던 부분 (익은 토마토 부분 bfs)
                q.append((k,i,j))

bfs() # arr upgrade

def solution():
    cnt = 0
    for floor in arr:
        for row in floor:
            for each in row:
                if each == 0: # 하나라도 익지 않은 토마토 발생
                    return -1
            # 0이 발생하지 않는다면 각각의 row에서 가장 큰 값이 계속 update
            cnt = max(cnt,max(row))
    return cnt-1 # 1부터 세기 시작했으므로 최종적으로 -1을 진행

print(solution())

