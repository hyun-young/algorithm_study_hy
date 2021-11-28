# numpy 사용 안 됨
from collections import deque
# import numpy as np

def solution(rows, cols, queries):
    # map = np.arange(1, rows*cols + 1)
    # map = map.reshape(rows,cols)
    map = [[0] * cols for _ in range(rows)]
    num = 0
    for i in range(rows):
        for j in range(cols):
            num += 1
            map[i][j] = num

    answer = []

    for query in queries:
        queue = deque()
        r1, c1, r2, c2 = query
        # 값 담아주기
        # ->
        for i in range(c1 - 1, c2):
            queue.append(map[r1 - 1][i])
        # ↓
        for i in range(r1, r2):  # 첫 꼭지점 빼고
            queue.append(map[i][c2 - 1])
        # ←
        for i in range(c2 - 2, c1 - 2, -1):  # 첫 꼭지점 빼고
            queue.append(map[r2 - 1][i])
        # ↓
        for i in range(r2 - 2, r1 - 1, -1):  # 첫 꼭지점, 마지막 꼭지점 빼고
            queue.append(map[i][c1 - 1])

        queue.rotate(1)  # idx 1씩 밀어주기
        answer.append(min(queue))  # 담긴 값 중 최솟값

        # ->
        for i in range(c1 - 1, c2):
            map[r1 - 1][i] = queue.popleft()
        # ↓
        for i in range(r1, r2):  # 첫 꼭지점 빼고
            map[i][c2 - 1] = queue.popleft()
        # ←
        for i in range(c2 - 2, c1 - 2, -1):  # 첫 꼭지점 빼고
            map[r2 - 1][i] = queue.popleft()
        # ↓
        for i in range(r2 - 2, r1 - 1, -1):  # 첫 꼭지점 빼고, 마지막 꼭지점 빼고
            map[i][c1 - 1] = queue.popleft()

    return answer