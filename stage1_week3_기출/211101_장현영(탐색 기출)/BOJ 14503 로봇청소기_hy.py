"""
함수 구현하여 왼쪽으로 돌 때마다 방향값을 return
청소기 구현시 좌표 2로 설정
a,b,c,d 단계 모두 마치도록 청소기 play
cleaner 원소로 답 구하기

- 탐색 문제는 반복숙달이 중요함
- 기존에 풀었던 문제였으나 다시 풀어보니 매우 오래 걸림
채점 결과: 메모리 29200kb, 시간 68ms
"""


import sys

input = sys.stdin.readline
# x는 행(세로), y는 열(가로)
dx = [-1,0,1,0] #       북,동,남,서
dy = [0,1,0,-1] #왼쪽:   서,북,동,남
# 0-3,1-0,2-1,3-2

def turn_left(d):
    if d == 0:
        left_d = 3
    else:
        left_d = d - 1
    return left_d


# 청소기 가동시 그 좌표 2로 설정
# 벽은 1, 청소가능구역 0
def play(board,x,y,ld):
    cnt = 0 # 회전 수, 4번 인지 확인 하는 것
    cleaner = []
    while 1:
        # 1번
        board[x][y] = 2
        cleaner.append((x, y))
        # 2번
        ld = turn_left(ld)
        nx = x + dx[ld]
        ny = y + dy[ld]
        # a
        if board[nx][ny] == 0:
            cnt = 0 # 회전 수 초기화
            x, y = nx, ny
        else: # b
            cnt += 1
            if cnt == 4:
                back_x = x + dx[ld - 2]
                back_y = y + dy[ld - 2]
                # c
                if board[back_x][back_y] != 1:# 바라보는 방향을 유지한 채로 한칸 후진한다.
                    cnt = 0 # 회전 수 초기화
                    x, y = back_x, back_y
                else: # d
                    break

    cleaner = set(cleaner) # 중복제거
    return len(cleaner)


board = []
# 세로, 가로
n, m = map(int,input().split())
# 현재좌표, (r,c), 로봇방향 d
r,c,d = map(int,input().split())
for _ in range(n):
    board.append(list(map(int,input().split())))

print(play(board,r,c,d))
