"""
dp index 맞춰주기
오름차순 부분 수열의 길이 최댓값 갱신해주기
* 주의 : 정렬해서 문제풀면 답이 달라짐!

6
(0) 10 20 10 30 20 50
[0,  1, 2, 1, 3, 2, 4]

6
(0) 20 30 10 50 10 20
[0,  1, 2, 1, 3, 1, 2]

6
(0) 8 7 6 5 4 3
[0, 1,1,1,1,1,1]

dp에 들어가는 값은 자기 자신 앞까지 가능한 부분 증가수열 길이 최댓값

30864kb 196ms 정답
"""

import sys

input = sys.stdin.readline

n = int(input())
# 0을 더해서 dp index 맞춰주기
nums = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
# 0이 있어야 dp에 값 나타낼 수 있음

for i in range(1, n+1):
    for j in range(i): # i를 기준으로 그 전 값들 비교
        if nums[i] > nums[j]:
            # max 이유? 자기 자신 이전에 모든 값들과 비교했을 때 가장 큰 경우를 써야하므로
            dp[i] = max(dp[i],dp[j]+1)

#print(nums)
#print(dp)
print(max(dp))


