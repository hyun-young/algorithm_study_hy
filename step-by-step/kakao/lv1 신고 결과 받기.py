"""
같은 사람이 같은 신고하면 1번으로 간주
30분
"""
from collections import defaultdict

def solution(id_list, report, k):
    d = defaultdict(list)
    cnt = defaultdict(int)
    for each in report:
        a, b = each.split()
        if b not in d[a]:
            d[a].append(b)
            cnt[b] += 1 # 신고당한 횟수
    print(cnt)
    answer = []
    for name in id_list:
        mail = 0
        for candidate in d[name]:
            if cnt[candidate]>= k:
                mail += 1
        answer.append(mail)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(id_list,report,2))