

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    vps = list(map(str,input().rstrip()))
    result = 0 # result가 양수를 유지하면서 최종 0이면 괄호끼리 다 해결
    for i in range(len(vps)):
        if vps[i] == '(':
            result += 1
        elif vps[i] == ')':
            result -= 1
            if result < 0: # )가 더 많아지는 즉시 종료
                break
    print('YES') if result == 0 else print('NO')

