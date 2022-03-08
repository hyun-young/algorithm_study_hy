"""
0.5초 주의
왜 시간초과? 수열크기 n 2000, 질문 m 최대 100만이므로 O(m*n) 복잡도

61290kb 2260ms
"""

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]

# 길이 1
for i in range(n):
    dp[i][i] = 1

# 길이 2
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

"""
길이가 3 이상인 경우

양끝 숫자가 같고 그 사이 숫자들(dp[i+1][j-1])가 1인지 확인하기 
dp[1][5] --> 1,5번째 숫자가 같은지, dp[2][4]가 1인지 확인
"""

# 길이 3 이상
for j in range(2,n): # j는 두 숫자 간 차이
    for i in range(n-j): # i는 앞 숫자 (start)
        # 처음과 끝이 같고, 앞+1,뒷-1씩
        if nums[i] == nums[i+j] and dp[i+1][i+j-1] == 1:
            dp[i][i+j] = 1

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])
