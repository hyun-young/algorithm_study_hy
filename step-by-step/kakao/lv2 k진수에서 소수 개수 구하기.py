"""
40분 소요
prime_num에서 제곱근 +1에 시간 오래 걸림
"""


import math

def k_number(n, k):  # n을 k진수로 반환
    tmp = ""
    while n > 0:
        tmp += str(n % k)
        n //= k
    return ''.join(reversed(tmp))

def prime_num(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    k_num = k_number(n, k)  # k진수로 반환
    for i in k_num.split('0'): # k_num을 0을 기준으로 분할
        if i == "": continue
        answer += prime_num(int(i))
    return answer