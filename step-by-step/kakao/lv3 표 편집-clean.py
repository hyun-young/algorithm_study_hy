import heapq

def solution(n, k, cmd):
    # 현재 위치:right heap의 첫 번째 원소

    left, right, delete = [], [], []
    # 왼쪽은 최대값이 맨 앞에 위치하도록, 오른쪽은 최솟값이 맨 앞에 위치하도록 heap을 구성한다.
    for i in range(n):
        heapq.heappush(right, i)
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))

    for c in cmd:
        # U or D인 경우
        if len(c) > 1:
            move = int(c.split()[-1])
            # D(아래로)인 경우
            if c.startswith("D"):
                for _ in range(move):
                # 오른쪽 heap에서 왼쪽 heap으로 값을 이동시킨다.
                    if right:
                        heapq.heappush(left, -heapq.heappop(right))

            # U(위로)인 경우
            elif c.startswith("U"):
                for _ in range(move):
                    # 왼쪽 heap에서 오른쪽 heap으로 값을 이동시킨다.
                    heapq.heappush(right, -heapq.heappop(left))
        elif c == "C":
            # 값을 삭제하되, 가장 최근에 삭제된 값을 복구하기 쉽도록 stack 형태를 사용한다
            delete.append(heapq.heappop(right))

            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택하도록 한다.
            if not right:
                heapq.heappush(right, -heapq.heappop(left))
        elif c == "Z":
            # 삭제한 값 복구하기
            repair = delete.pop()

            # 현재 위치보다 값이 작을 경우 left에 넣는다
            if repair < right[0]:
                heapq.heappush(left, -repair)
            else:
                heapq.heappush(right, repair)
    result = []
    while left:
        result.append(-heapq.heappop(left))
    while right:
        result.append(heapq.heappop(right))
    result = set(result)
    answer = ["O" if i in result else "X" for i in range(n)]

    return "".join(answer)