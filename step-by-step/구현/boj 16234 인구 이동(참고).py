"""
1. bfs로 인구수, 연합나라, 좌표 저장
2. 인구수 차이값이 l이상 r 이하이면 visit
3. move_q를 통해 좌표 불러와서 총 인구수를 총 나라수로 나눈 값으로 변경(이 부분 구현실패)
4. 연합 여부를 반환해서 확인
5. 방문 안한 모든 나라 bfs로 검사
    bfs 0이면 더이상 연합할 수 없음 --> bfs 모두 더했을 때 0이면 연합한 횟수를 출력
https://chldkato.tistory.com/126
"""

from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    move_q = deque()
    q.append([x, y])
    c[x][y] = 1
    people, cnt = 0, 0
    while q:
        x, y = q.popleft()
        move_q.append([x, y])
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not c[nx][ny]:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    c[nx][ny] = cnt
                    q.append([nx, ny])

    while move_q:
        x, y = move_q.popleft()
        a[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while 1:
    q = deque()
    c = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                cnt += bfs(i, j)
    if not cnt:
        break
    ans += 1

print(ans)