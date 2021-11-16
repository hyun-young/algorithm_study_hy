# 도시개수 n, 통로 개수 m 보내고싶은 도시 c
# 둘째줄부터 m번만큼 통로 정보 x,y,z 입력받음
# node x에서 node y가 간선으로 연결되었고
# 그 통로로 전달되는 시간 z(arrow 위 정보)

import sys
import heapq
input = sys.stdin.readline


n, m, c = map(int, input().split())
# 노드 당 연결 정보를 튜플 형태로 입력 받을 것
graph = [[] for _ in range(n+1)]
distance = [1e9] * (n + 1)


for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
    graph[x].append((y, z))

def dijkstra(c):
   q = []
   heapq.heappush(q, (0, c))
   distance[c] = 0
   while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c)

# 노드의 개수
cnt = 0
# 도달가능 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != 1e9:
        cnt += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외하고 max 거리와 함께 출력
print(cnt - 1, max_distance)
