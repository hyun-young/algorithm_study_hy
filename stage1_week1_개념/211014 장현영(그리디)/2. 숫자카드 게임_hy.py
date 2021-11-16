n, m = map(int, input().split())
min_element = []
result = 0

for i in range(n): # n행만큼 진행
    # 데이터를 map 형태로 한번에 받기
    data = list(map(int, input().split()))
    min_element.append(min(data)) # n행의 data 중 가장 작은 값
    result = max(min_element) # 가장 작은 요소 중 큰 값으로 업데이트

print(result)