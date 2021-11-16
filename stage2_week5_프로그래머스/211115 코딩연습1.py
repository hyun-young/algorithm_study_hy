# 배상 비용은 각 선박의 완성까지 남은 일의 작업량 제곱합산값
# maxheap 구현해서 풀기

import heapq

def solution(no, works):
    heap_list = []
    if no >= sum(works):
        return 0

    for num in works:
        heapq.heappush(heap_list, (-num,num))

    for _ in range(no):
        num = heapq.heappop(heap_list)[1]-1
        heapq.heappush(heap_list, (-num, num))

    return sum([each **2 for each in works])

solution(2, [10,1248,155])