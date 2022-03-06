"""
왜 이분탐색? -- 수의 범위 너무 크다

최소, 최대 범위 구하고 이분탐색으로 범위 좁히기
n명을 심사할 수 있을 때까지 진행하기

34712kb 1144ms
일부 참고 : https://wwlee94.github.io/category/algorithm/binary-search/immigration/
"""

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

times = [int(input()) for _ in range(n)]

low = 1
high = m * max(times) # 가장 최악으로 긴 시간만 사용하는 것

while low <= high:
    mid = (low + high) // 2
    people = 0

    for each in times:
        people += mid // each
    print(people)
    print(mid)
    if people >= m:
        ans = mid
        high = mid-1
    else:
        low = mid +1
    print('-'*30)

print(ans)