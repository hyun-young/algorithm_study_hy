'''
x로 막혀있지 않고 갈 수 있는데 거리가 2이하이면 미준수(bfs로 구현)
모든 p를 q에 넣고, 맨하탄 거리 1이면서 'O'인 곳 q에 넣고 한번 더 확인해서 거리두기 2 확인하기
50분 소요
'''
from collections import deque


def able(each):
    arr = [list(each[i]) for i in range(5)]
    q = deque()
    visited = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P': #응시자
                q.append((0,i,j))
    while q:
        print(q)
        cnt,x,y = q.popleft()
        visited[x][y] = 1 # P에서만 바뀌도록 설정
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if arr[nx][ny] == 'P' and not visited[nx][ny]:
                    return 0 # 거리두기 미준수(cnt 0이든 1이든 여기서 걸러짐)
                elif arr[nx][ny] =='O' and cnt == 0: # 빈 테이블이면서
                    q.appendleft((cnt+1,nx,ny))

    return 1 # while문 전부 통과 (거리두기 준수)

def solution(places):
    ans = []
    for each in places:
        ans.append(able(each))
    return ans

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# 거리두기에 걸리는 경우
dx = [-1,1,0,0]
dy = [0,0,1,-1]

print(solution(places))