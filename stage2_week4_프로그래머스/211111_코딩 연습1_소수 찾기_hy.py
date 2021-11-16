from itertools import combinations


def solution(nums):
    comb = list(combinations(nums,3))
    ans = []
    answer = 0
    for each in comb:
        ans.append(sum(each))

    for num in ans:
        for j in range(2, num):
            # 자기 자신보다 1 낮은 숫자까지 약수 존재 확인하기
            if num % j == 0:
                break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))