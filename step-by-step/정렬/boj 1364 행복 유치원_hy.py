"""
티셔츠 비용: 각 조 최대,최소 차이
정렬되어있는 아이들의 키의 인접차이를 heap으로 저장
heap에서 가장 최솟값을 뽑아내는 조합들로 더한 값이 정답이 됨

67924kb 500ms
"""

import sys
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())
kids = list(map(int,input().split()))

result = []

choose = n-k

for i in range(1,n):
    heapq.heappush(result,kids[i] - kids[i-1])

cnt = 0
ans = 0
while cnt < choose:
    ans += heapq.heappop(result)
    cnt += 1

print(ans)