import sys

input = sys.stdin.readline

result_list = []
for _ in range(int(input())):
    name, score = map(str, input().split())
    result_list.append((name, int(score)))

result_list.sort(key= lambda x:x[1]) # 인덱스 1 기준 정렬
for x in result_list:
    print(x[0], end = ' ') #공백있게

