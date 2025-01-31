N = int(input())
A = list(map(int, input().split()))

A.sort()
answer = 0

for x in range(1,N+1):
    answer += sum(A[0:x])
print(answer)