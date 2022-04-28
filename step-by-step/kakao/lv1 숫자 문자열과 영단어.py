"""
20분 소요
"""


def solution(s):
    tmp = ''
    ans = ''
    for spell in s:
        if not spell.isdigit(): # 영어라면
            tmp += spell
            if tmp in eng: # 완성된 단어
                ans += str(dic[tmp])
                tmp = ''
        else: # 숫자는 그대로 넣어주기
            ans += spell
    return ans


nums = [i for i in range(10)]
eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
dic = dict(list(zip(eng,nums)))
print(dic)
print(solution('onetwo3fourfive67'))