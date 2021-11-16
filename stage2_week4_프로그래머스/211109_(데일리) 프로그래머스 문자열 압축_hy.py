"""
idea : 단위별로 자르기
ex) n개 단위면 앞에서 n개씩 range 이용해 split
연속으로 동일한 것이 나오면
전체 길이 -(n-1), 3개이상 동일하면 -n 씩 계산해주기
채점 결과 : 72 / 100
----
단순하게 풀다보니 치명적 단점 발견
- 연속 문자가 9개에서 10개 넘어가면 길이 1더해줘야됨 ex) 9ab --> 10ab
- 99개에서 100개 넘어가도 길이 1 더해줘야됨 ex) 99y --> 100y
- 테스트 케이스 고려해서 푼 결과 간신히 맞았다.
"""



def solution(s):
    if len(s) == 1:
        return 1
    ans = [len(s)] * (len(s) // 2)
    n = 1
    # 만약 문자열 길이가 10이면 6부터는 단위 의미 없어짐
    while n <= len(s) // 2:
        result = []
        dig_list = []
        for idx in range(0, len(s), n):
            result.append(s[idx:idx + n])
        flag = False
        cnt = 0
        digit = 0
        for j in range(1, len(result)):
            if result[j] == result[j - 1]:
                if not flag:  # 처음 접하는 경우
                    flag = True
                    cnt += (n - 1)
                    digit = 2
                else:  # 3개 이상 연속으로 만나는 경우
                    cnt += n
                    digit += 1
            else:  # 다르다면 false로 초기화
                dig_list.append(digit) # 그 전까지 계수 넣어주기
                flag = False
                digit = 0
        if flag:
            dig_list.append(digit)
        #print(dig_list)
        for i in range(len(dig_list)):
            if dig_list[i] // 1000 == 1: # 한 문자로 1000개 채워진 경우
                #print('here!')
                return 5 # 1000x
            elif dig_list[i] // 100 >= 1:
                #print('here!!')
                cnt -= 2
            elif dig_list[i] // 10 >= 1:
                #print('here!!!')
                cnt -= 1

        ans[n - 1] -= cnt
        n += 1
    #print(ans)
    return min(ans)

print(solution("xxxxxxxxxxyyy"))