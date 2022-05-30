"""
idea : 정렬을 시키고 앞에서 두개씩 번들로 비교하는 것이 제일 효율적
- 처음 풀 때는 반복문 돌때마다 sort를 진행하여 시간초과로 틀림
- heap 정렬로 값이 추가될 때마다 힙으로 처리하여 정렬시키기
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

if n == 1:
    print(0) # card 개수 1 일때 비교안하고 바로 종료
    exit(0)

ans = 0
while len(heap) > 1 :
    first = heapq.heappop(heap) # 맨 앞 원소 빠짐
    second = heapq.heappop(heap) # 맨 앞 원소 빠짐
    ans += first + second
    heapq.heappush(heap, first+second) # 번들 새로 넣어줌

print(ans)