# 스택 : 후입 선출개념,
# 설거지 그릇처럼 늦게 입력된 값부터 작업

import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    command = sys.stdin.readline().split() # 1개를 넣어도 리스트 형태로 반환
    if command[0] == 'push':
        stack.append(int(command.pop()))
    elif command[0] == 'pop':
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(int(len(stack) == 0)) # 값 자체가 1, 0으로 반환되도록!
    elif command[0] == 'top':
        print(-1) if len(stack) == 0 else print(stack[-1])

# 왜 sys.stdin.readline()을 사용하는가?
# input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
# 입출력 속도 비교 : sys.stdin.readline() > raw_input() > input()