"""
플로이드 워셔로 2차원 배열로 min값 구해서 하려고 했으나
채점 결과: 메모리 초과
클린코드에서 deque을 사용하여 deque에 x의 연결 정보를 넣고,
연결된 도시의 정보를 deque에 업데이트 하여 단방향 고려해 +1씩 더해나감

deque 사용 채점 결과 : 메모리 99848kb, 시간 2152ms 기록
- deque과 친해져서 메모리 효율을 높이자...!
"""

import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int,input().split())

x_array = [-1] * (n+1)
x_array[x] = 0

graph = [[] for _ in range(n+1)]


# 연결된 도로는 도시 별로 그래프에 추가(단방향임을 주의)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)


queue = deque([x])
#print(queue)

while queue:
    city = queue.popleft()
    #print('city', city)
    #print('graph[city]',graph[city])
    for idx in graph[city]:
        #print('array',x_array)
        if x_array[idx] == -1:
            x_array[idx] = x_array[city] + 1
            queue.append(idx)
        #print(queue)

flag = False
#print(graph[x])
for city in range(1, n+1):
    if x_array[city] == k: # 최단 거리가 k와 같으면 도시 출력
        print(city)
        flag = True

if not flag: # graph[x]에 k가 없는 경우 해당하지 않는 경우
    print(-1)
