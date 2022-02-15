"""
배치할 수 있는 공유기 간의 거리의 최솟값들 중 max값 조합 뽑기
1 4 8 --> 3,4,7 --> 3
1 4 9 --> 3,5,8 --> 3
1 8 9 --> 7,1,8 --> 1
1 2 4 --> 1,2,3 --> 1
... max값은 3!

출처 : https://tmdrl5779.tistory.com/119
"""

import sys

input = sys.stdin.readline

n,c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


low = 1 #?? arr[0]
high = arr[-1] - 1

while low <= high:
    wifi_cnt = 1
    mid = (low + high)//2
    wifi = arr[0] + mid
    # print('low',low)
    # print('high',high)
    # print('mid(한계값)',mid)
    # print('available wifi',wifi)
    for i in range(1,n):
        if arr[i] >= wifi:
            wifi_cnt += 1
            wifi = arr[i] + mid
    #
    # print('wifi',wifi_cnt)
    # print('c',c)
    if wifi_cnt >= c:
        low = mid + 1
        # print('mid higher')
    else:
        high = mid -1
        # print('mid lower')
    # print('--'*30)

print(mid)

