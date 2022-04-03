"""
pypy3로는 한번에 정답인데 python 3으로는 시간초과
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if n == 3:
    print(*arr)
    exit(0)

ans = []
min_result = sys.maxsize
for i in range(n-2):
    last = arr.pop()
    low,high = 0, len(arr)-1 # index를 찾아가는 방식
    while low < high: # 두 용액을 오름차순으로 넣어야 하므로, low와 high가 같아지면 안됨
        mixed = arr[low] + arr[high] + last
        if abs(mixed) < min_result:
            min_result = abs(mixed)
            ans = [arr[low],arr[high],last]
        if mixed < 0:
            low += 1
        else:
            high -= 1
        if not min_result:
            break
    if not min_result:
        break

print(*ans)

