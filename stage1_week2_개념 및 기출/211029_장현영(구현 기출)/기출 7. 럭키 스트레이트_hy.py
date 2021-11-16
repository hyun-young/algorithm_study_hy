"""
idea
- 짝수 자릿수가 나올때 앞 뒤 비교해서 덧셈결과 같으면 lucky
"""

import sys

input = sys.stdin.readline

n = list(input().rstrip()) # string 형태를 list로 감싸기
first = n[:len(n)//2]; second = n[len(n)//2:]
score1 = 0; score2 = 0
for i in range(len(n)//2):
    score1 += int(first[i])
    score2 += int(second[i])

print('LUCKY') if score1 == score2 else print('READY')