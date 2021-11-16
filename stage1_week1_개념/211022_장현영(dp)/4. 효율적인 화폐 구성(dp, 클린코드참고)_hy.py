import sys

input = sys.stdin.readline

# 원하는 금액과 화폐 단위를 받으면 최소한의 화폐 개수를 출력한다.
# 불가능하면 -1
n, m = map(int,(input().split()))
bill = [int(input()) for _ in range(n)]
# 최소값을 찾으므로 초기값을 임의의 큰 값으로 설정
dp = [1e9] * (m+1)

dp[0] = 0

# 점화식 dp[i] = min(dp[i], dp[i-화폐단위]+1)
for i in range(n):
    for j in range(bill[i], m+1):
        # 화폐단위값~m 사이에 만드는 방법이 존재한다면
        if dp[j- bill[i]] != 1e9:
            dp[j] = dp[j- bill[i]]+1

print(dp)
print(-1) if dp[m] == 1e9 else print(dp[m])