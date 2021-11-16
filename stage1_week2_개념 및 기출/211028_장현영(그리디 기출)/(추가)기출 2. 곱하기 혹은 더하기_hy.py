"""
숫자로 구성된 문자열 s를 입력받으면 그 입력된 값 중 가장 큰 수를 만들기
연산은 왼쪽부터 오른쪽 순
idea
무조건 큰수를 만드는 것이므로 나눗셈과 뺄셈은 전혀 필요하지 않다.
대부분은 곱셈이 제일 크게 증가하나, 0,1이 나오면 덧셈으로 진행한다.
"""

import sys

input = sys.stdin.readline

num_string = input()

# 첫 번째 값은 무조건 더하고 출발
ans = int(num_string[0])

for idx in range(1, len(num_string)):
    digit = int(num_string[idx]) # 숫자를
    # 앞선 연산의 결과가 1보다 작으면 덧셈, 현재 숫자가 0,1이어도 덧셈
    if digit <= 1 or ans <= 1:
        ans += digit
    else:
        ans *= digit
print(ans)

