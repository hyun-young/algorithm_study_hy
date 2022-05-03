"""
아이디 추천
-,_,.,알파벳,숫자만 사용 가능
.은 처음끝 연속 사용 불가
대문자
40분 소요
"""

def solution(new_id):
    new_id = new_id.lower() # 1
    able = ['-','_']
    temp = []
    dot = 0
    for i in new_id: # 2
        if i.isdigit() or i.isalpha() or i in able:
            temp.append(i)
            dot = 0
        elif i == '.': # 3
            if dot==0:
                temp.append(i)
            dot += 1

    # 4
    try:
        if temp[0] == '.': temp.pop(0)
        if temp[-1] =='.': temp.pop()
    except:
        return 'aaa'
    # 5
    if len(temp) == 0:
        return 'aaa' # 바로 반환
    # 6
    if len(temp) >= 16:
        temp = temp[0:15]
        if temp[-1] == '.': temp.pop()
    # 7
    if len(temp) <= 2:
        for _ in range(3-len(temp)):
            temp.append(temp[-1])

    return ''.join(temp)

new_id = "=.="
print(solution(new_id))