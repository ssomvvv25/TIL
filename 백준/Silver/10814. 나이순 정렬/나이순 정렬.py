N = int(input())
arr=[]
for i in range(N):
    [a,b] = map(str, input().split())
    a = int(a)
    arr.append([a,b])
arr.sort(key = lambda x : x[0]) # (a,b)에서 a만 비교

for i in arr:
    print(i[0], i [1])