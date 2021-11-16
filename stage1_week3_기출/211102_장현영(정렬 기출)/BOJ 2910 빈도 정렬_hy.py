"""
idea :
array에 대한 키 값 리스트씩 추가(중복제거 & 순서유지)
키 값 리스트를 dict 형태로 묶고 정렬해 출력
채점 결과: 메모리 29200kb, 시간 72ms
- 클린코드로는 dict를 한번에 try,except로 cnt와 value를 묶어버림
- dict형 반복문을 편하게 쓰는 법 익히기
"""


import sys

input = sys.stdin.readline

n,c = map(int,input().split())
array = list(map(int,input().split()))
value_list = [] # 들어온 순서의 값을 가리킴
result = [] # 최종 결과

# 순서대로 중복 제거하고 넣기
for i in range(n):
    if array[i] in value_list:
        continue
    else:
        value_list.append(array[i])

cnt_list = [0] * len(value_list)

for idx in range(len(value_list)):
    cnt = 0
    for origin in array:
        if value_list[idx] == origin:
            cnt += 1
    cnt_list[idx] = cnt

# 주의!! dict형은 첫번째 값은 유일한 키를 가져야함
# 따라서 value를 먼저 넣음
tmp = [[value_list[i], cnt_list[i]] for i in range(len(value_list))]
d =dict(tmp)
tmp_2 = sorted(d.items(), key=lambda x: -x[1]) # cnt 역순으로 정렬

for val, cnt in tmp_2:
    print('%s ' % val*cnt, end='') # 문자열로 출력하는 것이라 곱한 만큼 추가되어 출력!
