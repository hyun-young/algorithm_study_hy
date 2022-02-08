"""
경우의수 4^5
브루스포스

ex) 이동 예시
동쪽 이동 : 모든 행에 대해 n-1칸부터 0번째 칸까지 동쪽으로 움직이는 것 구현
서쪽 이동 : 모든 행에 대해 0번째 칸부터 n-1칸까지 서쪽으로 움직이는 것
남쪽 이동 : 모든 열에 대해 n-1행부터 0번째 행까지 남쪽으로 ..
북쪽 이동 : 모든 열에 대해 0행부터 n-1번째 행까지 남쪽으로 ..

서쪽으로 이동 시 (2 2 0 0) --> (4 0 0 0)이 되려면

- 0번째 칸을 마지노선으로 잡고 1번째 칸이 마지노선과 같으므로 합치고 그 자리는 0으로

서쪽으로 이동 시 (4 2 0 2) --> (4 4 0 0)이 되려면

- 0번째 칸이 마지노선이었으나 0이 아닌 수 중 가장 가까운 수가 같은 수가 아닌 경우이므로
 마지노선을 1번째 칸으로 설정하여 1번째 칸과 같은 3번째 칸을 합쳐주고 그자리는 0으로

왜 deepcopy를 쓰는가?
1. 한쪽으로 움직인 경우 후에 또 다른 쪽으로도 확인하려면 원본이 필요!!
2. 기존 맵을 복사해두고 그 맵을 이동하도록 하기 위함


출처 : https://hongcoding.tistory.com/126
"""

import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def move(board, dir):
    if dir == 0:  # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp

    elif dir == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

ans = 0
dfs(graph, 0)
print(ans)