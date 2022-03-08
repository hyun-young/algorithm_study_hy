"""
일단 4까지 세보고 점화식을 세워보자

1 3 7 17 41

7 = 3*2 +1
17 = 7*2 + 3
41 = 17*2 + 7

an = a(n-1)*2 + a(n-2)

34712kb 112ms 정답
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (100001)

dp[0] = 1
dp[1] = 3
dp[2] = 7
for i in range(3,n+1):
    dp[i] = 2*dp[i-1]%9901 + dp[i-2]%9901

print(dp[n]%9901)

