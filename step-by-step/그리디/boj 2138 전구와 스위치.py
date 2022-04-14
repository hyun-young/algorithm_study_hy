"""
https://burningjeong.tistory.com/409 (그림참고)
https://devlibrary00108.tistory.com/465 (풀이참고)
"""

n = int(input())

arr=list(map(int,input().rstrip()))
target=list(map(int,input().rstrip()))
if arr == target:
    print(0)
    exit(0)

def switch(bulb, flag):
    cnt = 0
    if flag: # 첫 번째 버튼을 눌렀음
        cnt += 1
        bulb[0] ^= 1
        bulb[1] ^= 1
    for i in range(1, n-1):
        if bulb[i-1] != target[i-1]: #다른 것이 나온다면
            cnt += 1
            bulb[i-1] ^= 1
            bulb[i] ^= 1
            bulb[i+1] ^= 1
    # 마지막 버튼 구현 (인덱스는 0~n-1로 n-2가 다를 때 마지막 버튼 사용)
    if bulb[n-2] != target[n-2]:
        cnt += 1
        bulb[n-2] ^= 1
        bulb[n-1] ^= 1
    if bulb == target:
        return cnt
    return 1e9

arr_copy = arr[:] # 복사 사용
ans1 = switch(arr,True)
ans2 = switch(arr_copy,False)

ans = min(ans1,ans2)
print(ans) if ans != 1e9 else print(-1)
