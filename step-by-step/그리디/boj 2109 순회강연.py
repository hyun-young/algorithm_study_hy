"""
33932kb 92ms 정답
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    p, d = map(int, input().split())
    arr.append((d, p)) # 순서 거꾸로

arr.sort()
queue = []
for each in arr:
    heapq.heappush(queue,each[1])
    if len(queue) > each[0]:
        heapq.heappop(queue)

print(sum(queue))
