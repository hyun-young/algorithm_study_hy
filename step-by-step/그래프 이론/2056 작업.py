"""
모든 작업을 완료하기 위한 최소시간 출력하기
indegree = 0인 노드부터 경로 시작

1. 진입차수 = 0인 노드 queue 넣기
2. queue에서 하나의 노드 (pop)
3. pop한 노드 위상 순서에 추가
4. pop한 노드 연결된 edge 삭제 (in_degree -=1로 구현)
5. 답 노드와 기존 times의 노드와 선행노드의 원래 답 더한 경우 와 현재 답을 비교

"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
times = [0] * (n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    in_degree[i] = tmp[1] # 후행 노드 개수
    for j in range(2,2+in_degree[i]):
        arr[i].append(tmp[j])

queue = deque()
ans = [0] * (n+1)
for i in range(1, n+1):
    if in_degree[i] == 0:
        ans[i] = times[i] # 처음 시간으로 update
        queue.append(i)

while queue:
    now = queue.popleft() # now : 진입노드 0인 것
    for node in arr[now]:
        in_degree[node] -= 1
        ans[node] = max(ans[now]+times[node], ans[node])
        if in_degree[node] == 0:
            queue.append(node)
print(max(ans))