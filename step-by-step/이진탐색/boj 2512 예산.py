"""
low = budget[0]으로 설정시 틀리는 반례

6
77 89 61 118 91 142
120

---> 부처 예산 중 최솟값과 상관없이 20이 max이므로 low를 1로 잡고 출발하기
30860kb 116ms 정답
"""

import sys

input = sys.stdin.readline

n = int(input())
budget = list(map(int,input().split()))
total = int(int(input()))

budget.sort()
low,high = 1,budget[-1]

while low <= high:
    mid = (low + high) // 2
    res = 0 # total과 비교할 값
    for each in budget:
        res += min(each, mid) # 넣는 값을 최소 mid로 진행

    #print('low',low)
    #print('high',high)
    #print('mid',mid)
    #print('res',res)
    if res > total: # 왼쪽선택 (high를 하향)
        high = mid-1
        #print('left')
    else:
        low = mid+1        # 오른쪽선택 (low를 상향)
        #print('right')
    #print('--'*30)

print(high)