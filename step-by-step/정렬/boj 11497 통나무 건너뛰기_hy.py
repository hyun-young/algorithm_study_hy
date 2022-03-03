"""
그리디 핵심:
n = 5라면 순서대로 02431 순으로 배치 (idx 2씩 차이 확인하기)
(43은 볼 필요 없음 35가 더 크거나 같은 차이이므로!)
n = 6이면 순서대로 024531 순으로 배치
(45도 볼필요없음, 53이 더 크거나 같은 차이이므로!)

31880kb 204ms 정답답"""

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    for i in range(2, n):
        if arr[i] - arr[i-2] > ans:
            ans = arr[i] - arr[i-2]
    print(ans)