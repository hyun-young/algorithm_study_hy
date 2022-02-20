"""
이것이 코딩테스트다 개선된 다익스트라 코드 참고

heap으로 최소값 계속 뽑아내면서 더 짧은(가격이 싼)곳으로 distance 갱신해주기

58136kb 372ms 정답
"""

import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, dest):
    heap = []
    heapq.heappush(heap,[0, start]) # 시작노드로 가는 비용 0
    distance[start] = 0
    while heap:
        # heap으로 비용이 최소인 곳을 뽑아낸다.
        cost,now = heapq.heappop(heap)
        if distance[now] < cost: # 처리된 것이라면 무시
            continue

        for each in arr[now]: # each--> [도착도시,비용]
            node, weight = each[0], each[1]
            tmp = cost + weight
            # 직선보다 우회가 더 짧은 경우만 새로 갱신해주기
            if tmp < distance[node]:
                distance[node] = tmp
                heapq.heappush(heap,(tmp, node))

    return distance[dest]



n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
distance = [1e9] *(n+1) # 초기값은 무한대로

for _ in range(m):
    i,j,c = map(int,input().split())
    arr[i].append([j,c])

start, dest = map(int,input().split())

print(dijkstra(start, dest))
