import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())

# 동서남북 구현 코드에 익숙해지기 위해 반복 코딩할 것!

# n행 m열 2차원 리스트를 리스트 컴프리헨션으로 초기화
# 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적!
visit_list = [[0] * m for _ in range(n)]

# 모든 맵의 경계선은 바다(1)로 입력값을 받는다.
# 1. 현 좌표, 현 방향에서 반시계방향 순으로 갈 곳 정하기
# 2. 우선적으로 왼쪽에 방문 안한 곳 있으면 방향 회전 후 1칸 전진
# 3. 왼쪽이 모두 방문한 곳면 방향 전환만 하고 1단계로
# 4. 4방향 모두 방문했거나 바다로 되어있다면 방향 유지한 채로 1칸 후진 후 1단계로
# (이 때, 후진하는 칸이 바다라 못 간다면 움직임 stop)
x, y, direction = map(int, input_().split())
# 방향값 의미 : {북 동 남 서 : 0 1 2 3}
# 맵 정보 입력받기
gameMap = list()
for _ in range(n):
    gameMap.append(list(map(int, input_().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit_list[x][y] = 1 # 현재 칸은 방문처리
# 회전 함수
def turn_left():
    # direction을 dx,dy 리스트의 index로 활용한다.
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

# 방문한 칸 수를 출력하는 프로그램 만들기
cnt = 1 # 현재 칸은 방문
turn_time = 0 # 4번 회전했는지 여부 확인하기 위해!
while 1:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면에 가보지 않은 칸 존재하는 경우 이동(2단계)
    if visit_list[nx][ny] == 0 and gameMap[nx][ny] == 0:
        visit_list[nx][ny] = 1 # 그 칸으로 이동했다는 방문처리
        x = nx # 방문한 곳의 위치를 업데이트
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else: # 회전 후 이미 nx,ny이 방문한 곳이거나 바다인 경우
        turn_time += 1 # 뒤에 4단계에 해당 안되면 1단계로 돌아가는 형식
    if turn_time == 4: # 이미 4번 turn
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 4단계 후진하기
        if gameMap[nx][ny] == 0:
            x = nx
            y = ny
            visit_list[nx][ny] = 1
        else: # 뒤가 바다
            break
        turn_time = 0 # 회전 수를 0으로 초기화(1단계로 돌아감)

print(cnt)