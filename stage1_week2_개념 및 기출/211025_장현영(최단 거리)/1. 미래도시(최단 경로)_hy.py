import sys

input = sys.stdin.readline

n, m = map(int,input().split())
# 2차원 그래프 생성 (index 0은 사용 x라서 n+1개만큼)
# 0,1이 아닌 값은 초기화가 1e9(연결되지 않은 곳)
graph = [[1e9] * n+1 for _ in range(n+1)]

# graph[a][a] = 0으로 설정
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# 도로 정보 저장하기
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

# 플로이드 워셔 (0은 사용하지 않음)
# 직선 상태가 더 빠른가, 거쳐가는 것이 더 빠른가
# 직결이 되지 않은 상태이면 1e9 상태라 거쳐가는 것이 최소값이 저장됨
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번에서 출발하여 k를 거쳐 최종 목적지 x로 가는 여정 result
result = graph[1][k] + graph[k][x]

print(-1) if result == 1e9 else print(result)
