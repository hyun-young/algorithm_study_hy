"""
도둑루피 -- 소지한 루피가 감소
숫자가 적은쪽만을 향해 인접 위치로 1칸씩 이동

최소 금액 뽑아내기
(다익스트라 최단거리로 풀어보기)

32932kb 164ms 정답
"""

import sys
import heapq

input = sys.stdin.readline

def dijkstra(arr, rupee, n):
    heap = []
    heapq.heappush(heap,(arr[0][0], 0,0)) # 처음 arr값과 0,0 넣기
    while heap:
        # heap으로 비용이 최소인 곳을 뽑아낸다.
        cost,x,y = heapq.heappop(heap)
        if rupee[x][y] < cost: # 최소비용 처리된 것이라면 무시
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                ncost = arr[nx][ny]
                cost_sum = cost + ncost
                # 지금과 다음 루피값의 합이 최소비용 값보다 작으면 update
                if cost_sum < rupee[nx][ny]:
                    heapq.heappush(heap,(cost_sum, nx,ny))
                    rupee[nx][ny] = cost_sum

    return rupee[n-1][n-1]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

num = 1
while 1:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(n)]
    rupee = [[1e9] * n for _ in range(n)]

    ans = dijkstra(arr,rupee,n)
    print(f'Problem {num}: {ans}')
    num += 1