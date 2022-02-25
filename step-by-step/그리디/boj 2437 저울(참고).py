"""
측정할 수 없는 양의 정수 무게 중 최솟값 구하기

"""

import sys

input = sys.stdin.readline

n = int(input())
weight = list(map(int,input().split()))
weight.sort()

# 초기값 1로 세팅(답이 될 수 있는 최소 자연수)
# 맨 처음 가장 작은 값과 비교할 때 1보다 작을 순 없기에

standard_sum = 1

for each in weight:
    if each > standard_sum:
        break

    standard_sum += each

# standard_sum 측정 가능한 최댓값에 1이 더해진 값 == 측정 불가능한 최솟값
print(standard_sum)