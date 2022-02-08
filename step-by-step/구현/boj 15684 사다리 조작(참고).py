"""
기존 사다리에서 최소 개수 추가해서 모든 입출력이 같아지기
불가능하거나 최소개수가 3개 초과하면 -1
세로 개수 n, 연결다리(실선 가로 개수)m, 가로 연결 가능한 index 총 개수 h
클린코드
출처 https://whwl.tistory.com/34

"""

import sys

input = sys.stdin.readline


def make_line(start,cnt):
    global ans
    if cnt == min_cnt:
        if is_same():
            ans = cnt
        return # 재귀종료 표기
    for i in range(start, h): # 그릴수 있는 index만큼 반복
        for j in range(n-1):
            # (i,j) 위치에 사다리가 없고, (i,j±1)에도 사다리가 없는 곳
            if not ladder[i][j-1] + ladder[i][j] + ladder[i][j+1]:
                # 사다리 놓기
                ladder[i][j] = 1
                make_line(i, cnt+1)
                # 함수 재귀가 끝나면 사다리 다시 원상복구 시키기
                ladder[i][j] = 0

# 모든 입출력이 같은지 확인하는 함수
def is_same():
    # h행 n열로 1열부터 시작
    for j in range(n):
        tmp = j #
        for i in range(h):
            if ladder[i][tmp]: # 오른쪽 방향으로 이어져있는가
                tmp += 1
            elif ladder[i][tmp-1]: # 왼쪽 방향으로 이어져있는가
                tmp -= 1
        # 하나라도 원래 번호로 돌아오지 않으면 false
        if tmp != j:
            return False
    return True

# 세로n, 가로m, 세로선마다 가로선 놓을 수 있는 위치의 개수 h
n,m,h = map(int,input().split())

ladder = [[0]*n for _ in range(h)]
for _ in range(m):
    # (b)  --(a번째 가로선)--  (b+1)
    # 1 1 이면 첫번째 가로선이 1,2 연결
    # 2 5 이면 두번째 가로선이 5,6 연결
    # 6 3 이면 여섯번째 가로선이 3,4 연결
    a,b = map(int,input().split()) # 가로선
    ladder[a-1][b-1] = 1

ans = 10000

for min_cnt in range(4): # 최소 개수가 3개까지 이므로
    make_line(0,0)
    if ans != 10000:
        print(ans)
        break
else:
    print(-1)




