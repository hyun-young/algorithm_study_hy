import sys

input = sys.stdin.readline

n = int(input())
product = list(map(int,input().split()))
product.sort()
m = int(input())
find_item = list(map(int,input().split()))


def binary_search(array, target, a, b):
    # array는 정렬된 상태!
    while a <= b:
        mid = (a + b) // 2 # 중앙값
        # array[mid]이 중간점 인덱스를 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            b = mid - 1 # 끝지점을 mid-1로 설정(이진 탐색)
        else:
            a = mid + 1 # 시작점을 mid+1로 설정(이진 탐색)
    return None # 찾을 수 없음 None 반환

for item in find_item: # 찾고자하는 item을 target에 넣기
    result = binary_search(product, item, 0, n-1)
    print('no', end= ' ') if result==None else print('yes', end= ' ')
