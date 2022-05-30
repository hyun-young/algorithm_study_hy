"""
사거리 내/외 구분해서 확인
"""

import sys
from collections import deque

input = sys.stdin.readline

l = int(input()) # 전체 길이
able, damage = map(int,input().split()) # 사거리,살상력
bomb = int(input()) # 지뢰
zombie = [0]+[int(input()) for _ in range(l)] # 인덱스만큼 떨어져있는 좀비 체력
alive = 0 # 아직 체력 남은 좀비(총으로 사살 불가일 때)

q = deque()
if zombie[1] <= damage: q.append(0)
else:
    q.append(zombie[1])
    alive += 1

# 사거리 내에 있는 좀비부터 q 삽입
for i in range(2,min(able, l)+1):
    if alive == 0: #
        hp = zombie[i] - damage*i # 좀비 체력
        if hp <= 0: q.append(0) # 총으로 죽일 수 있음
        else:
            q.append(hp)
            alive += 1
    else:
        hp = zombie[i] - damage * (i - alive) # 지뢰 사용 횟수만큼 데미지 빼주기
        if hp <= 0: q.append(0)
        else:
            q.append(hp)
            alive += 1

# 처음 사거리 외 좀비 q 삽입
# (진행하면서 사거리에 있을 때 지뢰유무에 따라 데미지가 달라지므로 주의)
for i in range(able, l):  # 만약 able >= l이면 for문 안돌고 바로 q 완성
    hp = zombie[i+1] - damage * (able - alive)
    if q.popleft():
        if bomb > 0:
            bomb -= 1
        else:
            print('NO')
            exit(0)
        if hp <= 0:
            q.append(0)
            alive -= 1
        else:
            q.append(hp)
    else:
        if hp <= 0:
            q.append(0)
        else:
            q.append(hp)
            alive += 1

while q:  # q를 비우면서 확인
    if q.popleft():
        alive -= 1
        if bomb > 0:
            bomb -= 1
        else:
            print('NO')
            exit(0)
print('YES')







"""
시간초과
cum = [0]*l
z = deque(zombi)
cum_q = deque(cum)
while q:
    z = q.popleft()
    dam = cum_q.popleft()
    print(dam, z)
    if dam >= z:
        shoot = min(len(q),able)
        for j in range(shoot): # 총발사
            cum_q[j] += damage
    else:
        cnt += 1 # 지뢰 사용
    if cnt > bomb: # 쓸 수 있는 지뢰 초과
        flag = False
        break
    print(q)
print('YES') if flag else print('NO')
"""