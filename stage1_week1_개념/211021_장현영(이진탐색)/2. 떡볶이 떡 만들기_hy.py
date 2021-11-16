import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height_list = list(map(int, input().split()))

# a,b는 시작과 끝
a = 0; b= max(height_list)

ans = 0
while a <= b:
    # 떡 길이 합계
    total = 0
    cut = (a + b) // 2 # 중앙값(떡을 자르려고 하는 기준)
    # array[mid]이 중간점 인덱스를 반환
    for item in height_list:
        if item > cut:
            total += (item - cut)
    # total이 요구량 m에 못미치는 경우
    if total < m:
        b = cut - 1 # 끝지점을 mid-1로 설정(이진 탐색)
    # total이 요구량보다 충분한 경우
    else:
        a = cut + 1 # 시작점을 mid+1로 설정(이진 탐색)
        # ans를 cut으로 기록하기
        ans = cut # 계속 반복 진행시 최대한 덜 자르도록 설계

print(ans)

