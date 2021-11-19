import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 원소있는 리스트에서 최소 힙 쓰려면 heapify 필수
    while len(scoville) > 1:
        #print(scoville)
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        print(first, second)
        if first >= K:
            return answer
        heapq.heappush(scoville, first + second*2)
        answer += 1
    if scoville.pop() >= K: # 다 돌고 마지막 값으로 판단
        return answer
    else:
        return -1

print(solution([109,100,3,51,7,76],90))