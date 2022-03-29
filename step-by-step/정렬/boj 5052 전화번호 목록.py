"""
일관성 여부를 확인하기
(한 번호가 다른 번호의 접두어 인 경우가 없어야 함)
https://codingspooning.tistory.com/160
"""

import sys
input = sys.stdin.readline

flag = True
for _ in range(int(input())):
    n = int(input()) # 전화번호 목록 - 문자열
    arr = list(input().rstrip() for _ in range(n))
    arr.sort()
    for i in range(n-1): # 문자열로 정렬되었으므로 바로 옆만 비교
        if arr[i] in arr[i+1][:len(arr[i])]:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")
    flag = True
