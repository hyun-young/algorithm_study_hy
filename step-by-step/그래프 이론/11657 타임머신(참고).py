import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bus = []
for _ in range(m):
    a, b, time = map(int, input().split())
    bus.append((a, b, time))
dist = [1e9] * (n+1)


def bf(start):
    dist[start] = 0
    for k in range(n):
        for i in range(m):
            city, ncity, time = bus[i]
            if dist[city] != 1e9 and dist[ncity] > dist[city] + time:
                dist[ncity] = dist[city] + time
                if k == n-1:
                    return True
    return False

if bf(1):
  print('-1')
else:
  for i in range(2, n+1):
    if dist[i] == 1e9:
      print('-1')
    else:
      print(dist[i])