"""
옮기는 수 최소가 되도록 정렬하기
오름차순으로 정렬하면 가능한 문제이므로 lis으로 접근
최장 증가 부분 수열
증가 부분 수열이 아닌 경우인 곳만 배치하면 되므로 전체에서 max값 배기
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = [0]+[int(input()) for _ in range(n)]

dp = [0]*(n+1)

# 최장 증가 부분 수열
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]: # arr[0]=0이므로 최솟값 1
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))