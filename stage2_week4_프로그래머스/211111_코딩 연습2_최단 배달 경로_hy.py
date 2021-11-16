"""
특정 지점에서의 모든 노드간의 최단 경로를 구할 때는
플로이드 워셔가 아닌 다익스트라(모든 간선의 길이가 양수)를 사용해야 하나 구현하지 못함
"""

def solution(N, road, K):
    answer = 0
    graph = [[1e9] * (N + 1) for _ in range(N + 1)]
    # 자기 자신은 0으로 초기화
    for i in range(N + 1):
        graph[i][i] = 0

    for each in road:
        # 여러 도로가 있을 수 있으므로 최소값으로 update
        minimum = min(graph[each[0]][each[1]], each[2])
        graph[each[0]][each[1]] = minimum
        graph[each[1]][each[0]] = minimum

    # 플로이드 워셔 최단 경로 찾기
    # 거쳐간 경로가 빠른가, 직선도로가 빠른가를 업데이트
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 1번 마을의 배달 가능 여부 확인
    for each in graph[1]:
        if each <= K:
            answer += 1
    return answer


road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]

print(solution(6,road,4))