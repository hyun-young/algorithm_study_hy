def solution(n,a,b):
    if a > b:
        a,b = b,a
    answer = 0
    while a < b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2 # 다음 번호
    return answer





print(solution(256,1,4))