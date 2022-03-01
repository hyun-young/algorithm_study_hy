"""
1. 1년이 지날때마다 arr값을 바꿔주는 함수(defaultdict로 바다개수세고 반영해주기)
2. 영역이 2개로 나뉘었는지 최종 확인

출처 : https://m.post.naver.com/viewer/postView.naver?volumeNo=27365964&memberNo=33264526

"""

import sys
from collections import deque,defaultdict

input = sys.stdin.readline

def bfs(x,y,arr,visited):
    q = deque()
    ice = defaultdict(int)
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny]: # 주변이 바다인 경우
                    ice[(x,y)] += 1 # 좌표의 주변 바다 cnt
                elif arr[nx][ny] > 0 and not visited[nx][ny]: # 주변이 빙산인 경우
                    visited[nx][ny] = 1 # 방문 등록
                    q.append((nx,ny))
    return ice

# n행 m열
n,m = map(int,input().split())
arr = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

# arr list 받기
for i in range(n):
    arr.append(list(map(int, input().split())))

def solution():
    year = 0
    while 1:
        visited = [[0]*m for _ in range(n)] # n행 m열
        is_split = 0 # 쪼개졌는가?
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0 and not visited[i][j]: # 현 위치가 빙산이면서 업데이트 안된 곳
                    ice = bfs(i,j,arr,visited)
                    is_split += 1 # 여기서 이게 왜 +1?????
        if is_split > 1:
            return year
        for (x,y),cnt in ice.items():
            if arr[x][y] < cnt:
                arr[x][y] = 0
            else:
                arr[x][y] -= cnt
        year +=1

print(solution())

