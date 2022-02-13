"""
필기 1등, 실기 1등 기준으로 순위 만족하는 애들만 뽑기

필기 기준 오름차순 후 실기에서 신입사원에 해당하는 사람만 cnt하기

힙 쓰는 이유와 언제 힙을 쓰는가?
1. 시간복잡도 메모리 모두 잡을 수 있다. (삽입, 삭제에 필요한 복잡도 O(log N), 최대 최소까지 복잡도 O(1))
2. 간단한 정렬과 최소(최대)값을 뽑아서 비교할 때는 heap으로 구현하여 뽑아내는 것이 빠름

힙 트리 나무위키
https://namu.wiki/w/%ED%9E%99%20%ED%8A%B8%EB%A6%AC
heappop --> 46256kb 5300ms ~ 6000ms
sort    --> 46256kb 4200ms ~ 4600ms
"""


import sys
import heapq
input = sys.stdin.readline


t = int(input())
for i in range(t):
    n = int(input()) # 지원자
    rank = []
    for i in range(n):
        a, b = map(int, input().split())
        heapq.heappush(rank,(a,b))
    #rank.sort() #(면접 1등이 맨앞으로)
    # 신입사원 출력
    cnt = 0
    standard = n # 기준
    #for f, s in rank: #first, second
    while rank:
        f,s = heapq.heappop(rank)
        if s == 1:
            cnt += 1
            break
        elif s <= standard: # 처음이 기준이 되도록
            cnt += 1
            standard = s # 면접1등이 기준이 되도록 second 기준 갱신
    print(cnt)