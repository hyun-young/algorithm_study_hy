"""
2명 이상 주문만 코스에 포함 가능
코스는 result의 길이로 가능한 숫자들

tmp_list = sorted(list(each))
여기서 정렬 안해주면 (X,W)와 (W,X)를 다르게 인식하여 COUNT가 안됨
"""
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    max_len = 1
    # 예3처럼 max_len보다 큰 경우는 for문 돌릴 필요 없기에 max값 확인해주기
    for each in orders:
        max_len = max(max_len,len(each))

    for i in course:
        if i > max_len:
            break
        cnt_d = defaultdict(int)
        for each in orders:
            tmp_list = sorted(list(each)) # 주문이 정렬된 상태가 아니므로 정렬 반드시 필요
            comb = list(combinations(tmp_list,i))
            for c in comb:
                cnt_d[c] += 1
        cnt_d = sorted(cnt_d.items(), key=lambda x: -x[1])
        print(cnt_d)
        able_cnt = cnt_d[0][1] # 가장 많이 사용된 개수 뽑아내기
        if able_cnt < 2:
            continue
        for tup,num in cnt_d:
            temp_str = ''.join(tup)
            if num < able_cnt:
                break
            answer.append(temp_str)
    answer.sort()
    print(answer)
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders,course)