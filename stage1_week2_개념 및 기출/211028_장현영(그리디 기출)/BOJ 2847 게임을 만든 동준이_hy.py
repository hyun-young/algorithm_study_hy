"""
idea
마지막 스코어를 기준으로 스코어 계산 진행
while문 n-1번의 반복(한번 반복 진행마다 pop으로 원소 한개씩 빠짐)
모든 점수는 자연수이므로 기준이 1이 되면 값을 빼면 안됨
last라는 기준을 세워서 -1씩 반복하여 빼주는데, last는 0이 되지 않도록 if문
cnt에 값에서 last만큼 빼준값을 계속 더해줌
채점 결과: 정답, 메모리 29200KB, 시간 72ms
"""

import sys

input = sys.stdin.readline

n = int(input())
score_list = [int(input()) for _ in range(n)]

last = score_list.pop()
cnt = 0

while len(score_list):
    if last > 1:
        last -= 1
    if score_list[-1] >= last:
        cnt += (score_list.pop()- last)

print(cnt)