"""
모든 vertex i,j
단순하게 갈수 있는지 없는지 확인하는 문제
특정 지점에서 최단 경로 -- 다익스트라
모든 지점 경로 == 플로이드 워셔(3중 반복문)

32932kb 340ms 정답
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 이미 갈 수 있는 것말고 거쳐갈 수 있는가?
            if (arr[i][k] + arr[k][j]) > 1:
                arr[i][j] = 1

for each in arr:
    print(*each)



