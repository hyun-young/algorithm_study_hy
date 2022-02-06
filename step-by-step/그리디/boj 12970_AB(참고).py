"""

a = 전체 n개중 a의 개수, b = 전체 n개 중 b의 개수
A (a-1) + B(b-remain) + A(1) + B(remain)
n = 10       k와 비교
a  b
0 10	= 0
1 9	    = 9
2 8	    = 16       	here(k=10), remain= 2  ABBBBBBABB (8+2)
3 7	    = 21	    here(k=19), remain= 5  AABBABBBBB (7+7+5)
4 6	    = 24        here(K=24), remain= 6  AAA(0)ABBBBBB (4*6)
5 5	    = 25        here(K=25), remain=5   AAAA(0)ABBBBB (5*5)
6 4     = 24

30864KB, 68ms
"""

import sys

input = sys.stdin.readline


def solution():
    n,k = map(int,input().split())

    a = 0
    b = n
    while a*b < k and b > 0:
        a += 1
        b -= 1

    if k == 0:
        return 'A'*n
    elif b == 0:
        return -1
    print('a,b',a,b)
    remain = k - (a-1)*b

    return 'A'*(a-1) + 'B'*(b-remain) + 'A' + 'B'*remain

print(solution())