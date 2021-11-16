def solution(n):
    answer = ''
    while n > 0:
        n, r = divmod(n, 3) # n//=3, r= n%3
        if r == 0:
            answer += '4'
            n -= 1          # 3진법 수로 계산하기 위해 n-1로 계산해서 나타내기
        else:
            answer += str(r)
    return answer[::-1]

print(solution(4+9+27+81)) # 11111