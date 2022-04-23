"""
휴게소 위치 1~l-1
n+m < l
지어야 하는 휴게소는 m개
거리에 맞게 지어야 하므로 거리를 mid 값으로 나눈 값을 카운트해서 m개가 되면
그 mid값은 처음 나왔을 때가 최대이면서 최소인 값
"""

# 정답은 휴게소 위치가 아니라 최소간격이어야 함
# //2 식으로 넣는 것이 아님
# 휴게소가 2개 넣을 수 있고, 0(시작) 500 501(끝) 이라 할때

# 0 (125) (250) 500 501 --> 250 (x)
# 0 (167) (333) 500 501 --> 167이 정답

import sys


input = sys.stdin.readline

n,m,l = map(int,input().split())

arr = [0,l]+list(map(int,input().split()))
arr.sort()
low,high = 1,l-1 # low가 0부터 하면 mid가 0이 될 수 있으므로(간격이 0일 수 없음) 1부터 출발
while low <= high:
    mid = (low+high)//2
    cnt = 0
    for i in range(1,n+2):
        if (arr[i]-arr[i-1]) > mid: # 기준점부터 넘는 gap
            cnt += (arr[i]-arr[i-1]-1)//mid
            # -1: 이미 설치한 곳 제외하고 몇 개 세울수 있는지 cnt
    #print('mid,cnt,m',mid,cnt,m)
    if cnt > m: # 간격을 늘려서 cnt를 줄여야 한다.
        low= mid+1
    else:
        # 간격을 줄여서 cnt를 늘려야 한다.
        # (답을 충족하므로 간격을 더 줄이면서 최대가 되는 값 확인해보기)
        high = mid-1
        ans = mid
print(ans)

