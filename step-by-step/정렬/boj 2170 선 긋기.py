"""
p1,p2 움직이면서 판단해보기
python3,pypy3기준 코드결과 시간초과,정답 둘다 해당

"""

import sys

input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()#key=lambda x : (x[0],-x[1]))

p1,p2 = arr[0]
for s,e in arr[1:]:
    if p2 < s: # 이전 point들과 독립된 선이라면 새로 기준 세우기
        ans += (p2-p1)
        print('append,p2,p1',p2,p1)
        p1,p2 = s,e
    else:
        p2 = max(p2,e)

ans += p2-p1
print('last,p2,p1',p2,p1)
print(ans)


"""
----------------------------------------
그리디 기준으로 풀려다가 답 틀림 반례 못찾음
"""
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
ans = 0
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : (x[0],-x[1]))

print(arr)
tmp_s,tmp_e = arr[0] # 가장 첫번째 끝점
tmp_s += 1
tmp_e += 1
for i in range(n):
    s,e = arr[i]
    if tmp_e == e or tmp_s == s:
        print('erase',arr[i])
        arr[i] = [s,s] # 취급 안할 arr[i]로 만들기
    tmp_s, tmp_e = s,e


print(arr)
cs,ce = arr[0]
ans = ce-cs
for s,e in arr[1:]:
    if s == e:
        continue
    ans += (e-s)
    if ce-s > 0:
        minus = min(ce,e) - s
        print('here',ce,s)
        ans -= minus
    cs,ce = s,e

print(ans)
"""