"""
전체 정사각형 개수에서 잘린 정사각형 개수 빼주기
최대공약수!!
잘린 사각형: gcd* (w/gcd + h/gcd - 1)
answer - (w+h-gcd)
클린코드 및 개념 참고 출처 https://leedakyeong.tistory.com/135#comment16270807
"""


def solution(w,h):
    answer = w*h
    gcd = gcd_f(w,h)
    return answer - gcd*(w//gcd + h//gcd - 1)

def gcd_f(x,y):
    while y > 0:
        tmp = y
        y = x%y
        x = tmp
    return x