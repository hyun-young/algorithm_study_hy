"""
0,1로 영역 채운 다음에 방향탐색으로 0개수 세기
bfs queue 사용
32420kb, 100ms 정답
"""

import sys
from collections import deque

input = sys.stdin.readline

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]


# 동서남북
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    q = deque()
    q.append(((y,x)))
    graph[y][x] = 1 # 첫 숫자
    cnt = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and not graph[ny][nx]:
                graph[ny][nx] = 1
                q.append((ny,nx))
                #print(ny,nx,"cnt",cnt)
                cnt += 1
    return cnt

cnt = 0

for _ in range(k):
    # x1,y1 -- 왼쪽 아래, x2,y2 -- 오른쪽 위
    # 좌표로 왼쪽아래가 (0,0) 오른쪽 위가 (n,m)임을 주의
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

#print(graph)
res = []
for y in range(m):
    for x in range(n):
        if not graph[y][x]:
            res.append(bfs(y,x))
            #print('---')

print(len(res))
print(*sorted(res))