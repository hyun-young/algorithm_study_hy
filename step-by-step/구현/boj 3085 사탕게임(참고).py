import sys
input=sys.stdin.readline

def check(arr):
    ans = 0
    for i in range(n):
        cnt=1
        ex=1
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]:
                cnt+=1
            else: cnt=1
            if ans<cnt:
                ans = cnt
            if arr[j][i] == arr[j-1][i]:
                ex += 1
            else: ex=1
            if ans<ex: ans=ex
    return ans

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(1, n):
        # 바꿔주기
        arr[i][j],arr[i][j-1]= arr[i][j-1],arr[i][j]
        temp = check(arr)
        if ans<temp: ans=temp
        arr[i][j],arr[i][j-1]= arr[i][j-1],arr[i][j]
        arr[j][i],arr[j-1][i]= arr[j-1][i],arr[j][i]
        temp=check(arr)
        if ans<temp: ans=temp
        arr[j][i],arr[j-1][i]= arr[j-1][i],arr[j][i]

print(ans)
