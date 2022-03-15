"""
indegree : 내 앞에 연결된 노드 개수 (나한테 들어오는 엣지 수)

indegree가 0인 것부터 줄 세우기
줄을 이미 세운 노드는 그래프에서 없애버리고,
삭제 node와 연결된 node는 indegree -=1

(heap으로 구현한 1766 문제집과 유사)

deque, list 비교시 약 2000kb 정도 차이 발생(시간은 거의 유사)
37680kb 272ms 정답
"""

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

in_degree = [0] * (n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    in_degree[b] += 1

queue = deque()
ans = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    ans.append(now)
    for node in arr[now]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            queue.append(node)
print(*ans)