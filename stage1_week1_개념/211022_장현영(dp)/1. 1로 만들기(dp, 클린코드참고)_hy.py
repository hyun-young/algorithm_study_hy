import sys

input = sys.stdin.readline

# 정수 x 받기
x = int(input())
# dp 테이블 초기화
dp = [0]* 1000001

# dp bottom-up
for i in range(2, x+1):
    # 현재의 수에서 1 빼는 경우로
    # 초기값을 i-1의 연산수 +1로 잡음
    # 예를 들어 i=4면 3의 최소 연산수에 + 1을 한것이 초기 값이 된다는 의미
    dp[i] = dp[i-1] + 1

    # 여기서 dp[i//_] +1의 +1의 의미는 _로 나눈 연산을 한번 진행했다는 의미
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])