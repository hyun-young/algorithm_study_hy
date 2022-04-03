import sys

input = sys.stdin.readline

def binary_search(arr, x):
    low,high = 0, len(arr)-1
    while low <= high:
        mid = (low+high) //2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    return len(arr) - (high+1) #index, 개수 차이 때문에 1 더해줌


n,h = map(int,input().split())
# even 석순, odd 종유석
even,odd = [],[]

for i in range(n):
    meter = int(input())
    if i % 2 == 0: #아래부터 높이 재기
        even.append(meter)
    else: #위부터 높이 재기
        odd.append(meter)

even.sort()
odd.sort()

ans = n # 장애물 최솟값
cnt = 0 # 구간 개수 세기
for spot in range(1,h+1):
    # 아래에 매달린 경우, 만족 길이 spot-1
    even_cnt = binary_search(even, spot-1)
    # 위에 매달린 경우니까 만족 길이가 h- spot(1~h)
    odd_cnt = binary_search(odd, h-spot)
    total = even_cnt + odd_cnt
    if total < ans:
        ans = total # 최소 장애물 갱신
        cnt = 1
    elif total == ans: # 현재 최솟값과 합계가 같은 값이면 구간 개수 1 증가
        cnt += 1

print(ans,cnt)
