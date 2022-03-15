"""
모든 경우 탐색하기
n,m의 최대 길이 8

출처 : https://seungwoolog.tistory.com/53
"""

import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def bfs(arr,queue,case):
    # 깊은 복사 사용하기, 반복되는 queue,arr 변경
    arr = copy.deepcopy(arr)
    queue = copy.deepcopy(queue)

    for a,b in case:
        arr[a][b] = 1

    # 바이러스 queue
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                arr[nx][ny] = 2 # 바이러스
                queue.append((nx,ny))

    return sum(row.count(0) for row in arr)

n,m = map(int,input().split())
arr = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
zeros = []
queue = deque()

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 0:
            zeros.append((i,j))
        elif temp[j] == 2:
            queue.append((i,j))
    arr.append(temp)

make_walls = list(combinations(zeros,3))
ans = 0

for case in make_walls:
    ans = max(ans,bfs(arr,queue,case))

print(ans)