"""
항상 내리막길로 가는 bfs 구현하기
bfs로 구현하면 큐 안에서 가장 높은 지점부터 방문하도록 설계해야 하므로
(그냥 진행하면 같은 곳을 계속 방문하게 되어 시간초과)
즉, dp로 답 구할때  두 경로 중 낮은 높이가 먼저 빠져나가면 dp 값 갱신 불가
"""

import sys
import heapq # 우선순위 q 사용

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def bfs(a,b):
    queue= [(-arr[a][b],a,b)]
    dp = [[0]*n for _ in range(m)]
    dp[a][b] = 1
    while queue:
        _,x,y = heapq.heappop(queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] < arr[x][y]: # 현재지점보다 낮은 곳으로만 이동
                if dp[nx][ny] == 0: # queue는 경로가 될 수 있는 모든 좌표당 1개씩만 넣되, 높은 곳부터 뽑아내기 위해 heap 사용
                    heapq.heappush(queue,(-arr[nx][ny],nx,ny))
                dp[nx][ny] += dp[x][y] # 현 위치에서 내리막길 가능 개수만큼 더해주기 위해

    return dp[m-1][n-1]

def dfs(x,y):
    if dfs_dp[x][y] != -1:
        return dfs_dp[x][y]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] < arr[x][y]:  # 현재지점보다 낮은 곳으로만 이동
            cnt += dfs(nx,ny)
    dfs_dp[x][y] = cnt

    return dfs_dp[x][y]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

m,n = map(int,input().split())
arr = []
dfs_dp = [[-1]*n for _ in range(m)]

for _ in range(m):
    arr.append(list(map(int,input().split())))

#print(bfs(0,0))
dfs_dp[m-1][n-1] = 1
print(dfs(0,0))