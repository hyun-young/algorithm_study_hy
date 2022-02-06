"""
n개 회의 중 회의실 가능 사용표 제작
시작 끝시간이 주어지고 최대 회의 가능 횟수

idea :
1. 종료가 빠른 회의 순서, 그 다음 시작이 빠른 순서대로 졍렬하기
2. 시종 비교, 기준시간을 update하면서 answer 찾기

채점결과: 57784kb, 300ms 정답
"""

import sys

input = sys.stdin.readline

t = int(input()) # test case

classes = []
ans = 0
standard = 0 # 비교문 기준 끝 시간
for _ in range(t):
    classes.append(list(map(int,input().split())))

# 1. 종료가 빠른 회의 순서대로 정렬
# (첫 기준을 세우고, 종료-시작 순으로 정렬된 classes에서 최대한 많은 시간을 넣기 위함)
classes.sort(key=lambda x: (x[1],x[0]))

# 2. 시종 비교, 기준시간을 update하면서 answer 찾기
for start, end in classes:
    if start >= standard: # 기준시간보다 시작이 더 나중이라면 able
        ans += 1
        standard = end # 기준 시간 새로 잡기

print(ans)

