def solution(v):
    x = []
    y = []
    answer = []
    for each in v:
        x.append(each[0])
        y.append(each[1])

    # x부터 넣기 위해 순차적으로 for 문
    for i in range(3):
        if x.count(x[i]) == 1:
            answer.append(x[i])
            break

    for i in range(3):
        if y.count(y[i]) == 1:
            answer.append(y[i])
            break

    return answer

solution([[1, 1], [2, 2], [1, 2]])
