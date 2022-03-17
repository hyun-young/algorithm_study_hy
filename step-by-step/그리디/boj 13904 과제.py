"""
남은 일 수가 가장 큰것부터 줄여가면서 남은 과제값 중 max 값 지우기
arr를 순차적으로 지우면서 남은 과제 중 최댓값 계산 가능
https://wjswhdgur123.tistory.com/55?category=411935
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
idx = 0
ans = 0

arr.sort(reverse=True)
tmp = 0

for date in range(arr[0][0], 0,-1):
    for j in range(n):
        if arr[j][0] >= date and arr[j][1] > tmp:
            tmp = arr[j][1]
            idx = j
        else:
            break
        if tmp != 0:
            ans += arr[idx][1]
            del arr[idx]
        tmp = 0

print(ans)
