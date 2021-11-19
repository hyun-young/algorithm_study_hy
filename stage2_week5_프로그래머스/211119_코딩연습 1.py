# a,b를 최대힙으로 구현한 뒤 하나씩 제거해주면서 답 찾기

import heapq

def solution(a, b):
    heap_b = []
    heap_a = []
    score = 0
    for i in range(len(b)):
        heapq.heappush(heap_b,(-b[i],b[i]))
        heapq.heappush(heap_a,(-a[i],a[i]))

    for _ in range(len(a)):
        if heap_a[0][1] < heap_b[0][1]:
            heapq.heappop(heap_b)
            score += 1
        heapq.heappop(heap_a)

    return score

solution(a,b)