# 나이트의 현재 위치를 입력 받으면 이동할 수 있는 위치 확인

import sys

input_data = sys.stdin.readline()

# 아스키 코드 이용해서 a부터 순서대로 진행됨을 확인하고,
# 정수형으로 열 값 변환
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 8방향
knight = [(-2,-1), (-2,-1),
          (-1,-2),(-1,2),
          (1, 2), (1,-2),
          (2, 1), (2, -1)]

dx = [-2, -1, 1, 2, -2, -1, 1, 2] # 행 이동
dy = [-1, 1, 2, -2, -1, 1, 2, -2] # 열 이동

cnt = 0
# 8가지 위치 중 이동 가능한 경우를 cnt
for i in range(len(dx)):
    next_row = row + dx[i]# 행
    next_col = col + dy[i]# 열
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        cnt += 1

print(cnt)