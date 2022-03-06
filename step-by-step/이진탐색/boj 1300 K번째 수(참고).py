import sys
import heapq
from itertools import chain

input = sys.stdin.readline

n = int(input()) # 10^5
k = int(input())

low,high = 1,k

while low <= high:
    mid = (low + high) // 2
    temp = 0
    for i in range(1, n+1):
        temp += min(mid // i, n)  # mid 이하의 i의 배수 or 최대 N

    if temp >= k:  # 이분탐색 실행
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)







"""
# ex > n = 3, 123 123 , 1,2,3,2,4,6,3,6,9
a=[[0] * n for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i-1][j-1] = i*j

b = list(chain(*a))
heapq.heapify(b)
print(b)
for i in range(k):
    if i == k-1:
        print(heapq.heappop(b))
        exit(0)
    heapq.heappop(b)
"""