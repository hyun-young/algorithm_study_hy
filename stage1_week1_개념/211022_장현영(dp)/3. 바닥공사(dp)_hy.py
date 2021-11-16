import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

# dp[n] n*2에서 경우의수를 계산
# 1*2 한가지
dp[1] = 1
# 1*2를 2개, 2*1를 2개, 2*2를 1개 총 3번을 채울 수 있음
dp[2] = 3
for i in range(3, n+1):
    dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[n] % 796796)