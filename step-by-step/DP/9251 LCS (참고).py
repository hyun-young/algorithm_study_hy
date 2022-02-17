"""
lcs: 최장 공통 부분 수열
공통 부분 수열 중 가장 긴 것을 찾아라


ACAYKP CAPCAK --> ACAK가 정답

2차원 DP로 접근하기
두 수열의 길이만큼 DP 2차원으로 만들고 두 수열 조합에서 최장길이를 DP값으로 입력

"""

import sys

input = sys.stdin.readline


def LCS(x,y):
    xlen = len(x)
    ylen = len(y)
    dp = [[0]*(xlen+1) for _ in range(ylen+1)]

    for i in range(1, ylen+1):
        for j in range(1, xlen+1): # i를 기준으로 그 전 값들 비교
            if x[j-1] == y[i-1]: # 공통 수열이므로 같은 글자를 찾는다.
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # max값을 쓴이유는 자기자신 이전에 모든 값들과 비교했을 때 가장 큰 경우를 써야하므로


    return dp[-1][-1] # DP의 마지막 값을 출력한다.
# 리스트로 받기
word_1 = input()
word_2 = input()

ans = LCS(word_1, word_2)
print(ans)