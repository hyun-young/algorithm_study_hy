import sys

# 배열의 크기 N, 더하는 횟수 M, 특정 수 연속해서 K번까지 더할 때
# 가장 큰 수를 나타내기
n, m, k = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

data.sort()
a = data[-1]; b= data[-2]

# 반복되는 수열의 길이: k+1
# 전체 m번 중 최대 k번까지 더할 수 있으므로
# ex> 26번이고 최대 4번까지 더할 수 있으면
# k회 반복되는 수열이 등장 하는 횟수: m //(k+1) : 5
# 큰 수 a가 총 더해지는 횟수 m //(k+1) * k : 5*4=20
# aaaab aaaab aaaab aaaab aaaab || (a)
# 여기에 나머지 발생하면 a 추가 더하기 가능
cnt = m // (k+1) * k + (m % (k+1))

ans = a*cnt + b*(m-cnt)
print(ans)

