import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(speeds)):
        day = math.ceil((100 - progresses[i]) / speeds[i]) # 올림
        queue.append(day)
    tmp = queue.popleft()
    cnt = 1
    while queue:
        next = queue.popleft()
        if tmp < next:
            answer.append(cnt)
            cnt = 1
            tmp = next # cnt가 초기화될때 tmp를 업데이트
        else:
            cnt += 1
    answer.append(cnt) # 마지막 cnt 넣어주기
    return answer
