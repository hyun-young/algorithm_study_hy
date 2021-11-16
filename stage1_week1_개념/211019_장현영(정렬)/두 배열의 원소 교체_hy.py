import sys

input = sys.stdin.readline

# a 배열의 합을 최대로 만들기!
# a 배열의 최솟값을 b 배열의 최댓값으로 교체해주기

n, k = int(input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 내림차순 b는 오름차순
a.sort()
b.sort(reverse=True)

# a,b 모두 동일한 원소를 가지고 있으므로 크기비교를 통해 원소 교체
for i in range(n):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else: # a가 더 크다면 정렬된 상태이므로 반복문 더 이상 실행할 이유 x
        break

print(sum(a))

