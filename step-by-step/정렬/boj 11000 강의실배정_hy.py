"""
최소의 강의실로 모든 수업 가능하도록!
heap에 현재 연결되어 수업을 들을 수 없는 수업(종료시간으로)들을 집어 넣음
59876kb 412ms 정답
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
heap = []

for _ in range(n):
    start, end = map(int,input().split())
    classes.append((start,end))

classes.sort()

for s,e in classes:
    heapq.heappush(heap, e) # 종료시간 넣기
    if heap[0] <= s: # 가장빠른 종료시간이 s보다 작거나 같으면 udpate
        heapq.heappop(heap)
    #print(heap)

print(len(heap))