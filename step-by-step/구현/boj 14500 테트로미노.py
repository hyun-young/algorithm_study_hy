import sys

input = sys.stdin.readline
result = [0]

def solution(board, shape):
    ly = len(board) - len(shape) # 행
    lx = len(board[0]) - len(shape[0]) # 열
    # print('모양',len(shape),len(shape[0]))
    # print('board[0]', len(board[0]))
    # print('board', len(board))
    # print('lx',lx)
    # print('ly',ly)
    # 모양이 board 위에서 몇번 반복 될 수 있는 지
    for y in range(ly+1): #행
        for x in range(lx+1): # 열
            tmp = 0
            # 모양에서 1인 경우만 찾아서 더해주기
            for i in range(len(shape)): # 행
                for j in range(len(shape[0])): # 열
                    if shape[i][j] == 1:
                        tmp += board[y+i][x+j]
            if tmp > max(result):
                result.append(tmp)


# 4개의 숫자를 더한 것의 최댓값
# L,ㄹ,ㅗ,ㅁ,ㅡ 5종류
n, m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

line1 = [[1,1,1,1]]

square = [[1,1],
          [1,1]]
# L
l1 = [
    [1,0],
    [1,0],
    [1,1]]

l2 = [
    [0,1],
    [0,1],
    [1,1]]

l3 = [
    [1,1],
    [0,1],
    [0,1]]

l4 = [
    [1,1],
    [1,0],
    [1,0]]
# ㅗ
f1 = [[0,1,0],
      [1,1,1]]
f2 = [[1,1,1],
      [0,1,0]]
# z
z1 = [[1,1,0],
      [0,1,1]]
z2 = [[0,1,1],
      [1,1,0]]

shapes = [line1,l1,l2,l3,l4,f1,f2,z1,z2]
shape_t = []
for value in shapes:
    shape_t.append(list(map(list,zip(*value))))
#print(shape_t)
shapes.append(square)
shapes.extend(shape_t)
#print(len(shape))

for shape in shapes:
    solution(board, shape)

print(result[-1])