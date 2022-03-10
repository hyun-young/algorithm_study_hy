"""
양방향, 특정 지점에서 거리가 m이내 모든 아이템 습득 가능
아이템 최대 습득가능 개수

적은 n, 플로이드 워셔로 풀기 성공
30860kb 572ms 정답
"""


import sys

input = sys.stdin.readline

n,m,r = map(int, input().split())
items = list(map(int, input().split()))
arr = [[1e9]*n for _ in range(n)]
for _ in range(r):
    a,b,l = map(int, input().split())  # 연결된 지역의 번호(a, b), 길의 길이(i)
    # 양방향 값 갱신
    arr[a-1][b-1] = l
    arr[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                # 거쳐가는 것과 직선 루트 중 최단 거리 저장
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


ans = 0
for i in range(n):
    tmp = 0
    for idx,v in enumerate(arr[i]):
        if v <= m and v != 1e9:
            tmp += items[idx]
    tmp += items[i]
    ans = max(ans,tmp)

print(ans)