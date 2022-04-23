import sys
from collections import deque

input = sys.stdin.readline

def bfs(w):
    q = deque()
    visited = [0]*(n+1)
    visited[start] = 1
    q.append(start)
    while q:
        aa = q.popleft()
        if aa == end:
            return 1
        for bb,nk in arr[aa]:
            if w <= nk and not visited[bb]:
                visited[bb] = 1
                q.append(bb)
    return 0


n,m = map(int,input().split())
start,end = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a,b,k = map(int,input().split())
    arr[a].append((b,k))
    arr[b].append((a,k))

ans = 0
low,high = 0,int(1e6)
while low <= high:
    mid = (low+high)//2
    if bfs(mid): # 혜빈한테 갈 수 있으면 빼빼로 무게를 늘려서 확인하기
        low = mid+1
        ans = mid # 답이 되므로 update
    else: # 혜빈한테 갈 수 없다면 빼빼로 무게 줄여서 답이 되도록 설계
        high = mid-1

print(ans)
