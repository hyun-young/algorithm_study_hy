import sys

input = sys.stdin.readline

result_list = []
for _ in range(int(input())):
    result_list.append(int(input()))

result_list.sort(reverse=True)
for i in (result_list):
    print(i, end=' ')