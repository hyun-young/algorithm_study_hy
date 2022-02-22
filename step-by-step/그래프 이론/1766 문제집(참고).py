"""

문제 번호는 난이도 순 (높을수록 어려움)
문제 풀 순서 조건
1. n개 문제를 모두 푼다
2. 먼저 풀면 좋은 문제가 포함되면 반드시 그 문제를 먼저 푼다
3. 가능하면 쉬운 문제부터 푼다.

그래프 위상 정렬 (ex 대학교 선수과목 구조)

단방향이므로 indegree, outdegree로 나뉨
indegree(진입 차수): 한 정점으로 들어오는 간선 개수(선행 노드 개수)

indegree = 0인 노드부터 경로 시작

1. 진입차수 = 0인 노드 queue 넣기
2. queue에서 하나의 노드 (pop)
3. pop한 노드 위상 순서에 추가
4. pop한 노드 연결된 edge 삭제 (in_degree -=1로 구현)
5. 1-4 반복

위상정렬 개념 출처:  https://seohyun0120.tistory.com/entry/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC%EC%9D%B4%EB%9E%80-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
풀이 출처:          https://seongonion.tistory.com/121
"""

import sys
import heapq


input = sys.stdin.readline


n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    in_degree[b] += 1 # 후행 노드의 indegree 1씩 더하기
    arr[a].append(b) # 선행노드에 [후행노드들] 넣기

# heap으로 우선순위 queue 구현
queue = []
ans = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    now = heapq.heappop(queue)
    ans.append(now)

    for node in arr[now]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            heapq.heappush(queue, node)

print(*ans)