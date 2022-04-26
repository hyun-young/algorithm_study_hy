"""
홀수면 전체 타일 크기가 3*홀수 ==> 홀수이므로
2*1,1*2로 채울 수 없음 --> 0
가로 2써서 만드는 경우의 수 3
가로가 2씩 증가할 때 마다 가운데 H모양 고유 타일 2개씩 증가

https://suri78.tistory.com/103

"""

import sys

input = sys.stdin.readline
n = int(input())
if n % 2:
    print(0)
    exit(0)

dp = [0]*(n+1)
dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = 3*dp[i-2] + 2*sum(dp[:i-2])+2

print(dp[n])

