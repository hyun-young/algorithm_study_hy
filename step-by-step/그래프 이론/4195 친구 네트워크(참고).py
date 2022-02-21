"""
union-find 개념
서로소 집합 -- 공통 원소가 없는 두 집합

1. union 연산(서로 연결된 두 노드 확인)
 - a의 루트노드 a'와 b의 루트 노드 b'를 찾기(find)
 - a'를 b'의 부모노드로 설정 (a' < b')
2. 모든 union 연산을 처리할 때 까지 1 반복


이름 입력 받고 parents에 없는 이름이면 추가
두 이름을 합쳐 친구 관계로
현재까지 해당 친구관계를 포함해 같은 집합(부모가 같은)에 있는 원소 개수 출력

출처 : https://sungmin-joo.tistory.com/35

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 특정 원소가 속한 루트 노드 찾기
def find_parent(x):
    # 루트 노드일때 까지 찾아내기(종료조건) (키 = value)
    if parent[x] == x:
        return x
    # 원소가 root노드가 아니라면, 루트 찾을 때 까지 재귀
    parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합 union
def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a != parent_b:
        # 기준을 f2(b)로 잡기
        parent[a] = b # f1의 부모를 f2로 설정
        nums[b] += nums[a]  # f2의 친구 수에 f1 친구 수를 더함

t = int(input())
for _ in range(t):
    parent = dict()
    nums = dict()
    f = int(input())
    for _ in range(f):
        f1,f2 = map(str, input().strip().split())
        if f1 not in parent:
            parent[f1] = f1
            nums[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            nums[f2] = 1

        union_parent(f1,f2)
        print(nums[find_parent(f2)])
    #print('parent',parent)
    #print('nums',nums)
