"""
가방 오름차순으로 정렬 후 보석무게(최대 힙)를 넣으면서 가능한 경우만 heap으로
https://zu-techlog.tistory.com/44
"""

import sys
from heapq import heappop,heappush,heapify

input = sys.stdin.readline

n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
heapify(arr)
bags.sort()

ans = 0
queue = [] # 가격만 들어가는 queue(최대 힙으로 구현)
for each in bags:
    while arr and each >= arr[0][0]:
        heappush(queue, -heappop(arr)[1])
    if queue:
        ans -= heappop(queue)
    elif not arr:
        break
print(ans)