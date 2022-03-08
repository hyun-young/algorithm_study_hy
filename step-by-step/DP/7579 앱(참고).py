"""
냅색문제(최소비용 구하기)
1. 물건을 나눠 담는 문제 (분할가능 냅색)
2. 물건 못 나눠 담는 문제 (0,1 담는 여부로 판단하는 냅색)

dp[i][j] --> i번째 앱까지 중 j 코스트로 얻을 수 있는 최대의 메모리 값
(행: n, 열은 전체 코스트의 합만큼)
ex) dp[3][9] --> 3번째 앱까지 중 비용 9로 얻을 수 있는 최대 메모리

https://claude-u.tistory.com/445

47468kb 684ms 정답

"""

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

memories = [0] + list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))

dp = [[0]*(sum(costs)+1) for _ in range(n+1)]
ans = sum(costs) # 최악의 경우

"""
1. (비용 비교) 현재 앱의 비용이 j보다 클 경우 끄지 못하므로 이전 앱 값과 동일하게
2. (메모리 비교) 현재 앱 비용이 j보다 작거나 같다면 현재 앱 끈 뒤 메모리와 그대로 상태의 메모리값 비교  
"""
for i in range(1,n+1):
    memory = memories[i]
    cost = costs[i]

    for j in range(1, sum(costs)+1): # j는 1 ~ 최대 메모리까지의 값
        if j < cost: # 현재 j가 비활성화 조건에 충족 못하는 경우
            dp[i][j] = dp[i-1][j]
        else: # j-cost : 현재 j가 10이고, cost가 3이면 이전 앱까지에서 j가 7인 값의 메모리+ byte
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

        if dp[i][j] >= m: #메모리값이 비교값(m)을 충족한다면 결과 update
            ans = min(ans,j)

print(ans) if m!=0 else print(0)


