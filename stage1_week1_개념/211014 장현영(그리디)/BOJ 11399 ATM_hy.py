import sys

# 핵심: 가장 적은 소요시간 인 사람이 먼저 인출하기

n = int(sys.stdin.readline())
atm_list = list(map(int, sys.stdin.readline().split()))

atm_list.sort()
result = 0
for i in range(n): # n명
     # idx=0은 n번, idx=1은 n-1번씩.. idx=n-1은 1번 더해주기
    result += (n-i)*atm_list[i]

print(result)