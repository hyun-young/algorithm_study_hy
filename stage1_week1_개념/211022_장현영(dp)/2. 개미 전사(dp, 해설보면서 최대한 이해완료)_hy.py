import sys

input = sys.stdin.readline

# dp[원소의 개수] : 최댓값
# dp[0], target_list[0] 은 0으로 잡기
# dp[n] ==> n개의 원소일때 최댓값으로 정의
# dp[i]
# 1 ~ i-2까지의 최댓값에 i번째 원소가 추가된 값 vs
# 1 ~ i-1까지의 최댓값
# 이 둘을 계속 비교해가면서 n까지 끌어오기

n = int(input())
target_list = list(map(int, input().split()))
target_list.insert(0,0) # index와 번째 맞추기 위함
dp = [0] * 100 # n은 최대 100
# dp[0]은 취급 안함

# 원소 1개(선택의 여지 없이 첫 번째 target_list 원소)
dp[1] = target_list[1]
# 원소 2개일 때는(1,2번쨰 중 큰 값 1개만 선택)
dp[2] = max(target_list[1], target_list[2])
# 여기서부턴 반복문 출발
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + target_list[i], dp[i-1])

print(dp[n])