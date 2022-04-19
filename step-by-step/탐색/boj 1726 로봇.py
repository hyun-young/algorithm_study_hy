"""
go k, turn 둘 중 하나만 사용하기
right: 1234--> 3421
left : 1234--> 4312
"""
import sys

input = sys.stdin.readline
from collections import deque

def right(d):
    right_tmp = (0,3,4,2,1)
    return right_tmp[d]

def left(d):
    left_tmp = (0,4,3,1,2)
    return left_tmp[d]

def bfs(cx,cy,d):
    q = deque()
    dist = [[[0]*5 for _ in range(n+1)] for _ in range(m+1)]
    q.append((cx,cy,d))
    while q:
        x,y,d = q.popleft()
        if x == tx and y==ty and d==td:
            return dist[x][y][d]
        # k만큼 진행
        for k in range(1,4):
            dx, dy = dr[d]
            nx = x + dx*k
            ny = y + dy*k
            if not 0 < nx <= m or not 0 < ny <= n:
                break
            if arr[nx][ny]:
                break
            if not dist[nx][ny][d]: # 아직 방문한 적 없는 곳
                q.append((nx,ny,d))
                dist[nx][ny][d] = dist[x][y][d] + 1 # k만 달라지고 현재 x,y는 고정됨

        # 회전 # 방향을 3개를 선정해야 한다!!(2개만 선정해서 틀림)
        turn_list=[left(d),right(d),right(right(d))] # hd:180
        for nd in turn_list: # 세 방향
            if not dist[x][y][nd]: # 회전한 곳에서 업데이트 안됐다면
                cnt = 2 if nd == turn_list[-1] else 1
                dist[x][y][nd] = dist[x][y][d] + cnt
                q.append((x,y,nd))

# 동서남북(1,2,3,4)
dr = [None,(0,1),(0,-1),(1,0),(-1,0)]

m,n = map(int,input().split())
arr = [[1]*(n+1)]
for i in range(1,m+1):
    arr.append([1]+list(map(int,input().split())))

cx,cy,d = map(int,input().split()) # 현재 위치와 상태
tx,ty,td = map(int,input().split()) # 목표 위치와 상태

print(bfs(cx,cy,d))
