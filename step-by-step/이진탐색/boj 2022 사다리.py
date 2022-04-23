"""
find h
high를 min으로 --> max는 답(떨어진 거리)이 될 수 없음
"""

import sys
import math

input = sys.stdin.readline

# 실수형!
x,y,c = map(float,input().split())
low,high = 0,min(x,y)

# mid를 옮기면서 h를 c에 대입하여 최소오차 범위 내로 답 구하기

while (high-low) > 1e-6:
    mid = (low+high)/2
    h1 = math.sqrt(x*x-mid*mid)
    h2 = math.sqrt(y*y-mid*mid)
    h = (h1*h2)/(h1+h2) # mid를 이용해서 구한 h
    if h > c:
        low = mid
    else:
        high = mid

print("%.3f" %(round(mid,3)))