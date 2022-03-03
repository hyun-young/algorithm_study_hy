"""
n개 과제 중 과제 i, d(i)일이 걸리고 t(i)내로 끝내야 함
한번 시작한 것은 연속해서 진행
연속으로 과제 안할 수 있는 날이 최대 며칠인가(1일부터가 핵심)

13-6 = 7 이 정답이 아님!
3
d(i) t(i)
2     8
1     13
3     10
1~5 쉬고 6-7, 8-10,13에 과제하면 최대 5일 연속 쉬는 것

정답의 기준은 1~()일까지 쉬는가가 문제, 즉 1일부터 최대 몇일 쉬는가

시간이 오래걸림 : 167132kb 4664ms 정답
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []


# 받을 때 due(ti) 기준으로 받아서 정렬하기
for _ in range(n):
    term, due = map(int,input().split())
    heapq.heappush(arr,(due,term)) # 순서 반대로

first_due, first_term = heapq.heappop(arr)
ans = first_due-first_term # 기존 마감일에서 과제일만큼 최대한 미룬 값을 뺀 것이 ans 최댓값
sum_date = first_term # 총 과제 기간

while arr:
    due, term = heapq.heappop(arr)
    sum_date += term
    # 기준 마감일이랑 과제기간을 뺀 값과 기존 ans 비교해 더 적은 것으로 update
    ans = min(ans,due-sum_date)

print(ans)


