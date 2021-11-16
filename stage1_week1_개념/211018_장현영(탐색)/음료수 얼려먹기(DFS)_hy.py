# 얼음 얼릴 수 있는 공간, 상하좌우로 연결
# 그래프로 모델링 가능
# dfs 상하좌우 재귀를 통해 묶음 개수 찾을 수 있음

# 1. 특정 지점 상하좌우 본 후 값이 0이면서 아직 방문x인곳
# 2. 방문한 지점에서 다시 상하좌우 연결된 모든 지점을 방문할 수 있음
# 3. 2번 반복
# 결과값: 음료수를 몇번 채우는가(몇번 방문할 수 있는가?)
import sys

input = sys.stdin.readline

# n행 m열
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(graph)
# 특정 노드 방문 후 연결된 모든 노드들 방문
def dfs(x,y): # return은 T/F 형태
    # 경로 이탈 즉시 종료-- False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 방문 안했으면 방문처리하고, 상하 좌우 재귀 호출
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False  # 방문을 마친 후 false 처리

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# sys.stdin.readline() 주의사항
# 우리가 입력한 값을 모두 받기 때문에
# 문자열 끝에 입력한 개행문자(\n)도 같이 받으므로
# rstrip()을 붙여 주면 개행문자가 제거되어 정상 사용
