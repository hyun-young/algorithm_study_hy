import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
cheese=[list(map(int,input().split())) for _ in range(n)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]

def bfs():
    dq=deque()
    dq.append((0,0))
    visited=[[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    cnt=0
    while dq:
        y,x= dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=ny<n and 0<=nx<m):
                continue
            if cheese[ny][nx] ==0 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = 1
            elif cheese[ny][nx] == 1 and not visited[ny][nx]:
                cheese[ny][nx] = 0
                visited[ny][nx] = 1
                cnt += 1
    return cnt

res=[]
time=0
while 1:
    piece = bfs()
    if piece == 0:
        print(time)
        print(res[-1])
        break
    time += 1
    res.append(piece)