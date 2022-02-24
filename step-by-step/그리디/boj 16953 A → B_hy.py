"""
a를 b로
1. 2 곱하기
2. 1을 수의 가장 오른쪽에 추가 --> (8 --> 81)

b를 a에게 맞춰주기

불가능한 조건
A가 B보다 이미 큰 경우 OR B가 홀수면서 끝자리가 1이 아닌 경우
홀수면서 끝자리가 3,5,7,9이면 1을 붙이거나 2를 곱해도 절대 불가능

30864kb 76ms 정답
"""

import sys
input = sys.stdin.readline

cnt = 1
a, b = map(int, input().split())

# B를 A에게 맞춰주기
while 1:
    if b == a:
        break
    elif (b % 2 and b % 10 != 1) or b < a:
        cnt = -1
        break
    elif b % 10 == 1:
        b = (b-1)// 10 # 191 --> 19, 2321 --> 232
        cnt += 1
    else:
        b //= 2
        cnt += 1
print(cnt)