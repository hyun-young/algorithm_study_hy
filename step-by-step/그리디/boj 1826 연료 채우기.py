"""
remains 내의 모든 주유소 중 기름 가장 많은 곳을 택하기
35172kb 108ms 정답
"""

import sys,heapq
from collections import deque


input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int,input().split())))

target,remains = map(int,input().split())

cnt = 0
able_km = remains # 최초 remains 만큼 이동 가능
arr.sort()
q = deque(arr)
heap = []
while 1:
    if able_km >= target:
        break
    while q:
        dist,fuel = q.popleft()
        if dist <= able_km:
            heapq.heappush(heap, -fuel) # 최대 힙 위해 - 붙이기
        else:
            q.appendleft((dist,fuel)) # 다시 집어 넣고, q 끝내기
            break

    if not heap:
        cnt = -1
        break

    # 힙에 주유소 후보가 있다면 가장 큰 곳 하나만 충전할 것
    max_fuel = heapq.heappop(heap)
    max_fuel *= -1
    cnt += 1
    able_km += max_fuel


print(cnt)