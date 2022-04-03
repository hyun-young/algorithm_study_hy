"""
https://leunco.tistory.com/80
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(mid):
    q = deque()
    visited = [0] * (n+1)
    visited[start] = 1
    q.append(start)
    while q:
        curr = q.popleft()
        for area, limit in arr[curr]:
            # limit보다 낮으면서 갈 수 있는 곳을 q에 append
            if limit >= mid and not visited[area]:
                q.append(area)
                visited[area] = 1
    return visited[end] # 최종 지점 방문이 1인가 0인가

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
low,high = int(1e9),1
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))
    low = min(low,c)
    high = max(high,c)

start,end = map(int,input().split())

answer = low # 답은 전체 c 중 최소값부터 시작
# 이진 탐색
while low <= high:
    mid = (low+high)//2
    if bfs(mid): # 이동 가능, 가능한 중량 늘려보기
        answer = mid
        low = mid+1
    else: # 이동 불가, 가능한 중량 줄어보기
        high = mid-1

print(answer)