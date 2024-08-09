import sys
input = sys.stdin.readline
# 비내림차순..
def backtracking(x) : # 앞의 숫자와 비교해야하므로 파라미터로 넘겨줌
    if len(arr) == m: # array의 길이가 m과 같으면 답 출력
        print(*arr)
        return
    for i in range(x,n+1): # 파라미터로 받은 숫자보다 같거나 커야함
        arr.append(i) # 수를 더해주고
        backtracking(i) # 더한 수를 파라미터로 가지고 backtracking
        arr.pop() # 원 상태로 돌리기 위해 pop

n,m = map(int, input().split())
arr=[]
backtracking(1)
