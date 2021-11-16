# bfs: 너비우선 탐색(큐)
# 가까운 노드부터 탐색하는 알고리즘

# 방문처리 개념은 dfs 개념정리에서 확인
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문 안한 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번 더이상 실행 x까지 반복

# 재귀개념의 dfs보다 bfs가 처리속도가 더 빠르다.
# deque 라이브러리 O(N) 소요

from collections import deque

def bfs(graph, start, visited):
    # 큐 구현
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌때까지 계속 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 방문하지 않으면 queue에 삽입
                visited[i] = True # 방문 True

visited = [False] * 9
graph = [
    [],  # 빈리스트
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

bfs(graph, 1, visited)