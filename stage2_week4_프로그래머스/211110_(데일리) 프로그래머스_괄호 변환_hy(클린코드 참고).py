def recursive(p):
    if p == '':
        return ''

    for i in range(1, len(p) // 2 + 1):
        if p[0:i * 2].count('(') == p[0:i * 2].count(')'):
            a = p[0:i * 2]
            b = p[i * 2:]
            break

    if check(a):
        val = a + recursive(b)
    else:
        val = '(' + recursive(b) + ')'
        val += _reverse(a[1:-1])

    return val


def _reverse(a):
    table = {'(': ')', ')': '('}
    temp = ''
    for i in a:
        temp += table[i]

    return temp


def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()

    if stack:
        return False
    else:
        return True


def solution(p):
    if check(p):
        return p
    else:
        return recursive(p)