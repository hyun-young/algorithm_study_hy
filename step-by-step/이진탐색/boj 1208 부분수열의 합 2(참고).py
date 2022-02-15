"""
크기가 1 이상인 부분수열 중 합이 s와 같은 경우의 수 찾기

#
1. 절반씩 a,b 나눠서 각각 부분수열 구한다.
2. a 부분수열 하나 b 부분수열 하나 선택해서 모든 부분 수열을 구한다.
3. 부분수열 합을 arr에 저장
4. sum(a) sum(b) sum(a+b) 원소로 모든 부분 수열의 합 구한다.
출처 : https://ku-hug.tistory.com/190
"""

import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def getNum(arr, find):
    tmp = bisect_right(arr, find) - bisect_left(arr, find)
    return tmp

def getSum(arr, sumArr):
    for i in range(1, n+1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()



n,s = map(int, input().split())
arr = list(map(int, input().split()))

# 1
left, right = arr[:n//2], arr[n//2:]
leftSum, rightSum = [], []

getSum(left, leftSum)
getSum(right, rightSum)

print(leftSum)
print(rightSum)


ans = 0
for l in leftSum:
    find = s - l
    ans += getNum(rightSum, find)

ans += getNum(leftSum, s)
ans += getNum(rightSum, s)

print(ans)
