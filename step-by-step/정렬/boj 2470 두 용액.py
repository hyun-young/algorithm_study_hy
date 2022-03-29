"""
숫자를 정렬하고, low high를 idx 조절하여 모든 경우를 넣음
양 끝단의 절대값을 비교하여 더 큰 쪽이 0과 거리가 있는 경우이므로 인덱스를 가운데로 땡기기
ex
-900 -100 -50 60 901 902
1. -900,902
2. -900,901 (high -=1)
3. -900,60 (high -=1)
4. -100,60 (low +=1)
5. -50,60 (low +=1)

-7 -4 -3 1 2
1. -7 2 (low +=1)
2. -4 2 (low +=1)
3. -3 2 (low +=1)
4. 1 2 (low +=1)

-90 -20 -10 -5
1. -90 -5
2. -20 -5 (low +=1)
3. -10 -5 (low +=1)

"""

import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
heap = []
print(arr)
low,high = 0, n-1 # index를 찾아가는 방식
while low < high: # 두 용액을 오름차순으로 넣어야 하므로, low와 high가 같아지면 안됨
    mixed = abs(arr[low] + arr[high])
    if abs(arr[low]) > abs(arr[high]):
        heappush(heap,(mixed,arr[low],arr[high]))
        low += 1
    else:
        heappush(heap,(mixed,arr[low],arr[high]))
        high -= 1
print(heap)
_,a,b = heappop(heap)
print(a,b)
