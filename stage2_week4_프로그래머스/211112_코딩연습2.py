def solution(arr):
    if len(arr) == 0:
        return True
    new_list = [i for i in range(1,len(arr)+1)]
    arr.sort()
    answer = True if arr == new_list else False
    return answer
