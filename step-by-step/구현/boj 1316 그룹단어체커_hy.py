
"""
다시 그 글자 쓰면 그룹단어가 아님!
그룹단어 정의: 1개 이상 사용시 연속으로만 사용된 단어
그룹 단어의 개수를 출력하는 프로그램 작성

채점: 30864kb, 72ms 정답
"""

import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    flag = True
    result = []
    word = input() # string
    for alpha in word:
        # result가 빈 리스트인 경우(처음 사용된 경우)
        if len(result) == 0:
            result.append(alpha)
            #print('1',alpha)
        # 알파벳이 result에 없거나 마지막 result 알파벳이 같은 알파벳인 경우
        elif alpha not in result or alpha == result[-1]:
            result.append(alpha)
            #print('2',alpha)
        # 그룹단어가 아닌 경우
        else:
            #print(alpha, 'now false')
            flag = False
    #print(flag)
    if flag: # 단어 기준으로 flag가 True이면 cnt+=1
        cnt += 1
print(cnt)