"""
방향으로 2차원 배열로 생각해 전진 후진해서 더해주기
내 풀이는 방향에 따라 층 별로 계산하려 했으나 구현 실패
"""

import itertools


def solution(n):
    map = [[0] * n for _ in range(n)]  # n*n배열로 만들어주기
    r, c = -1, 0  # 0,0으로 출발하기 위해 초기값 -1,0으로
    cnt = 1
    for direction in range(n):
        for _ in range(direction, n):
            if direction % 3 == 0:
                r += 1  # 행 증가 이동 (제일 처음 값 0,0)
            elif direction % 3 == 1:
                c += 1  # 열 증가 이동
            else:
                # 행,열 감소이동
                r -= 1
                c -= 1
            map[r][c] = cnt
            cnt += 1

    # 2차원 원소 1차원으로 만들기 위해 chain 사용
    return [i for i in itertools.chain(*map) if i != 0]
