"""
컨베이어 벨프가 2n, 로봇이 n자리에서 out
https://jainn.tistory.com/81
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
res = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1]=0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
            robot[-1]=0 #이 부분도 로봇 out -> 0임
        if not robot[0] and belt[0]:
            robot[0] = 1
            belt[0] -= 1
        res += 1
        if belt.count(0) >= k:
            break
print(res)
