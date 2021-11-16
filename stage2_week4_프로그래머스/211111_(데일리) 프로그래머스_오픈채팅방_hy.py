"""
tmp[0]: act, tmp[1]:id, tmp[2]:nickname
"""
def solution(record):
    d = dict()
    answer = []
    for command in record:
        tmp = command.split()
        if tmp[0] =='Enter' or tmp[0] == 'Change':
            # {아이디:닉네임}, 마지막 닉네임이 최종 업데이트 됨
            d[tmp[1]] = tmp[2]

    # 최종 출력을 위해 answer에 append
    # change는 출력요소 없음
    for command in record:
        tmp = command.split()
        if tmp[0] == 'Change':
            continue
        elif tmp[0] == 'Enter':
            answer.append(f'{d[tmp[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{d[tmp[1]]}님이 나갔습니다.')
    return answer