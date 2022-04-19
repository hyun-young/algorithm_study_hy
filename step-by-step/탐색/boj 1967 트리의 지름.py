"""
트리의 지름: 모든 경로 중 가장 긴 길이
사이클이 없기에 갈 수 있는 두 노드 사이 경로는 1개뿐
"""
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
res = 0
def dfs(root,v):
    global res
    for node,weight in arr[root]:
        if dist[node] == -1: # not visited
            dist[node] = v + weight
            res = max(res,dist[node])
            dfs(node, v+weight)


n=int(input())
arr = [[] for _ in range(n+1)]
ans = 0
for _ in range(n-1):
    a,b,v = map(int,input().split())
    arr[a].append((b,v))
    arr[b].append((a,v))

dist = [-1] * (n+1)
dist[1] = 0
dfs(1,0)
deep_idx = dist.index(res)
# 가장 깊숙한 곳을 root노드로 해서 dfs 다시 돌리고 답 구하기
dist = [-1] * (n+1)
dist[deep_idx] = 0
dfs(deep_idx,0)
print(res)

