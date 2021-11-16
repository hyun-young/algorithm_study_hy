import sys

n = int(sys.stdin.readline())
cnt = 0
while True:
    if (n % 5) == 0: #5로 나누어 떨어지는 순간 다 털어버리고 종료
        cnt += (n//5)
        print(cnt)
        break
    # 5로 나누어 떨어지지 않은 경우므로 3을 빼면서 봉지 1개씩 cnt
    n -= 3
    cnt += 1
    if n < 0:
        print(-1) # 3,5를 약수로 갖지 않는 경우
        break