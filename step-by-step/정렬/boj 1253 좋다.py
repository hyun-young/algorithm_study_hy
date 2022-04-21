"""

"""
import sys

input= sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = []
cnt = 0
for i in range(n):
    arr_c=arr[:]
    target = arr_c.pop(i) # target을 만들기 위해서 target 수를 쓰면 안됨
    p1,p2 = 0,n-2
    while p1 < p2:
        two = arr_c[p1]+arr_c[p2]
        if two == target:
            cnt += 1
            break
        if two < target:
            p1 += 1
        else: p2 -= 1


print(cnt)