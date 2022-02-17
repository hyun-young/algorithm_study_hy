"""
모든 무게에 대해 최대가치 저장

2차원 DP로 접근하기
두 수열의 길이만큼 DP 2차원으로 만들고 두 수열 조합에서 최장길이를 DP값으로 입력

https://kils-log-of-develop.tistory.com/247
https://ssooyn.tistory.com/19
"""

import sys

input = sys.stdin.readline

n,k = map(int,input().split())
weight = [0]
scores = [0]
for _ in range(n):
    w,v = map(int,input().split())
    weight.append(w)
    scores.append(v)

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+scores[i])

        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])