"""
n(문자열 길이), k(조건만족하는 개수)
s의 길이는 , a,b로 구성
조건 : 인덱스 순서 기준 A B를 만족하는 인덱스쌍이 k개

틀렸습니다.

- 실패한 이유
1. 약수, 덧셈으로 묶어서만 생각하다보니 remain에 대한 접근 못함
2. A,B에 대한 개수 접근식 자체가 잘못됨
"""

import sys

input = sys.stdin.readline

n, k = map(int,input().split())

def find_divided(k): # 약수 찾고 배열
    temp = list()
    for i in range(1,k+1):
        if i > k//i:
            break
        if k % i == 0:
            temp.append((i,k//i,sum([i, k//i])))
    return temp


# 6 7 반례 발생
def find_divided2(k): # 합산 찾고 배열
    temp = list()
    for i in range(1,k+1):
        temp.append((i,k-i))
    return temp

if k == 0:
    print('A'*n)
    exit(0)
if k == 1:
    ans = 'B' * (n-k-1) + 'AB'
    print(ans)
    exit(0)

comb = find_divided(k)


#print(comb)

cnt1 = 0
try:
    for each in comb:
        if each[2] <= n:
            cnt1 = n-each[2]
            cnt2, cnt3 = each[0],each[1]
            break
    ans = 'B'* cnt1 + 'A'*cnt2 + 'B'*cnt3
except:
    if len(comb) == 1: # 약수가 1인 소수일 때
        comb2 = find_divided2(k)
        cnt4 = -1
        for each in comb2:
            if each[0]*each[1] < k:
                cnt4, cnt5 = each[0],each[1]
                break
        ans = 'A' + 'B'*cnt4 + 'A' + 'B'*cnt5 #??
        print(ans)
        exit(0)
    ans = -1

print(ans)