"""
수 묶기
적절히 묶어서 합이 최대가 되도록 구현해봐라
0은 아예 배제시키기
곱셈이 가능하므로 절댓값 큰 순으로 음수 양수 구분지어서 계산

34460kb 92ms 정답
"""

import sys
from collections import deque

input = sys.stdin.readline

# 무조건 짝수개로 맞추기
def queue_calc(q):
    res = 0
    while q:
        f = q.popleft()  # first 절대값 제일 큰 수
        s = q.popleft()  # second 절대값 그 다음수
        if f*s > f+s:
            res += (f*s)
        else:
            res += (f+s)
    return res


n = int(input())

zero = False
ans = 0

pos = []
neg = []
for _ in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else: # 0이 하나라도 포함된다면(flag 처럼 사용)
        zero = True

# 절댓값 큰 순으로 각각 정렬
pos.sort(reverse=True)
neg.sort()

# 시간 효율을 위해 deque 사용
pos_q = deque(pos)
neg_q = deque(neg)


# 음수처리
if len(neg) % 2: # 홀수개
    rest_neg = neg_q.pop()
    if not zero: # 0이 존재한다면 0 곱해주는 식으로 마지막 없애기
        ans += rest_neg

# 양수 처리
if len(pos) % 2:
    rest_pos = pos_q.pop()
    ans += rest_pos

ans += (queue_calc(pos_q) + queue_calc(neg_q))

print(ans)