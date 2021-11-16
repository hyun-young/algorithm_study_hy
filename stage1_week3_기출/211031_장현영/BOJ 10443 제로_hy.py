import sys

input = sys.stdin.readline

result_list = []

for i in range(int(input())):
    num = int(input())
    if num:
        result_list.append(num)
    elif len(result_list):
        result_list.pop()

print(sum(result_list))