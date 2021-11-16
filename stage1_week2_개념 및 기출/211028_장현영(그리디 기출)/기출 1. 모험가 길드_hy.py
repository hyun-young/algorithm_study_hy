"""
그룹은 그룹내 공포도가 제일 높은 사람의 공포도 만큼 사람수 필요
모든 모험가를 그룹에 넣을 필요 없음
그룹 수 최댓값 구하기
idea
공포도 sort하기
순차적으로 들어온 점수가 그룹의 인원보다 같거나 작은 경우 그룹에 넣기
"""

import sys

input = sys.stdin.readline

n = int(input())
scare_score = list(map(int,input().split()))
scare_score.sort()

num = 0
group = 0 # 멤버수

for score in scare_score:
    group += 1
    if score <= group:
        num += 1
        group = 0 # 새 그룹을 편성하기 위해 초기화

print(num)