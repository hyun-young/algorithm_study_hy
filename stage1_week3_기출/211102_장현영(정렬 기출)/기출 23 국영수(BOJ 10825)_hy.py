"""
조건
국어 내림차순, 영어 오름차순,수학 내림차순, 이름 사전순
idea : lambda 적극적으로 이용하기
채점결과 : 메모리 64568KB, 시간 548MS
- 클린코드(44284KB, 360MS)는 어차피 이름만 출력하면 되므로,
info_list.append((100-int(tmp[1]),int(tmp[2]),100-int(tmp[3]),tmp[0]))
로 넣고, 한번에 info_list.sort()하고 이름만 출력함(lambda 안쓰고 푸는 법)
"""


import sys

input = sys.stdin.readline

info_list = []
n = int(input())
for _ in range(n):
    tmp = list(map(str, input().split()))
    for i in range(1,4):
        tmp[i] = int(tmp[i]) # 점수는 int형 전환
    info_list.append(tmp)

info_list.sort(key=lambda x : (-x[1], x[2], -x[3],x[0]))

for i in range(n):
    print(info_list[i][0])