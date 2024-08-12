n = int(input())
arr = list(map(int, input().split()))

d = [0]*n # 동적 프로그래밍을 위한 배열 d 초기화
d[0] = arr[0] # 첫 번째 원소는 초기화

for i in range(1,n): # 두 번째 원소부터 마지막 원소까지 반복
    d[i] = max(arr[i],d[i-1]+arr[i]) # 현재 원소를 선택했을 때 최대합을 계산
print(max(d))