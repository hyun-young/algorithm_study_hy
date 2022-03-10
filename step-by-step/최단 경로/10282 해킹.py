"""
의존하는 관계(기본 단방향이나 특정 edge 양방향 가능),
의존성과 컴퓨터 번호, 몇대의 컴퓨터, 시간을

49416kb 1040ms 정답"""


import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap,[0, start]) # 시작노드로 가는 비용 0
    times[start] = 0
    while heap:
        # heap으로 비용이 최소인 곳을 뽑아낸다.
        curr_sec,target = heapq.heappop(heap)
        if times[target] < curr_sec: # 처리된 것이라면 무시
            continue
        for each_sec, com in arr[target]:  # 각 [시간,타겟컴퓨터]
            tmp = each_sec + curr_sec
            # 직선보다 우회가 더 짧은 경우만 새로 갱신해주기
            if tmp < times[com]:
                times[com] = tmp
                heapq.heappush(heap,(tmp, com))

    return times

t = int(input())
for _ in range(t):
    n,d,c = map(int,input().split())
    arr = [[] for _ in range (n+1)]
    for _ in range(d):
        # s초 후 b-->a 감염
        a,b,s = map(int,input().split())
        arr[b].append([s,a])
    times = [1e9 for _ in range(n+1)]
    result = dijkstra(c) # c부터 시작
    max_time = 0
    ans = 0
    for each in result:
        if each != 1e9:
            ans += 1
            if each > max_time:
                max_time = each
    print(ans, max_time)
