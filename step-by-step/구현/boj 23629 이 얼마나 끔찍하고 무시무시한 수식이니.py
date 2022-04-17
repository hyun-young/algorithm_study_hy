import sys
import math

input = sys.stdin.readline

eng = ['ZERO','ONE','TWO','THREE','FOUR','FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
nums = [str(i) for i in range(10)]
calc = ['+','-','*','/','=']
e_to_n = dict(zip(eng,nums))
n_to_e = dict(zip(nums,eng))
s = input().rstrip()
# s를 변환해주기
for word, num in e_to_n.items():
    s = s.replace(word, num)
ans1 = s[:]

for x in s:
    if x == 'x':
        s = s.replace('x', '*')

# 숫자랑 인자랑 분리하기
in_a_row = 0
arr=[]
tmp = ''
for single in s:
    if single in calc:
        in_a_row += 1
        # madness 조건: 연속인자 또는 숫자로 변환안된 s
        if in_a_row > 1 or not tmp.isdigit():
            print('Madness!')
            exit(0)
        arr.append(tmp)
        arr.append(single)
        tmp = ''
    else:
        tmp += single
        in_a_row = 0

current = '+'
res = 0
for each in arr:
    if each.isdigit():
        if current != '/':
            res = eval(str(res)+current+each)
        else:
            if res > 0:
                res = eval('math.floor({}/{})'.format(res,each))
            else:
                res = eval('math.ceil({}/{})'.format(res,each))
    else:
        current = each
        if current == '=':
            break

ans2 = ''
for each in str(res):
    if each == '-':
        ans2 += each
    else:
        ans2 += n_to_e[each]

print(ans1)
print(ans2)