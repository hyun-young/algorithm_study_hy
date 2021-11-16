"""
idea
- flag(괄호 안 상황)일 때는 뒤집기 안하기
- 리스트 형태의 ans을 이용해서 계속 거꾸로 넣거나 바르게 넣어 전체 result에 추가해주기
채점 결과: 정답, 메모리 30764KB, 시간 104ms
"""

import sys

input = sys.stdin.readline

S = input().rstrip() # 엔터 개행키 \n 빼주기
ans = []
flag = False  ### 괄호 상태
result = str()


for char in S:
    if char == '<':
        if len(ans) != 0:  # 괄호 안이고, ans에 들어있는 경우
            ans = ans[::-1]  # 거꾸로 넣기
            for i in range(len(ans)):
                result += ans[i]
            ans.clear()  # 다 넣었으면 비워주기
        flag = True  # 괄호 안임을 의미
        result += char
    elif flag:  # 괄호 안 상태였다면
        result += char  # 괄호안에 그대로 넣어주기
        if char == '>':  # 괄호 안 상태였다면
            flag = False  # 괄호 밖 상황으로
    elif char == ' ':
        ans = ans[::-1]  # 거꾸로 넣어주기
        for i in range(len(ans)):
            result += ans[i]
        ans.clear()
        result += char
    else:
        ans.append(char)

if len(ans) != 0:  # 아직 ans에 남아있다면
    ans = ans[::-1]  # 거꾸로 넣어주고
    for i in range(len(ans)):
        result += ans[i]
    ans.clear()
print(result)