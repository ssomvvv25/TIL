# 대칭 차집합 = (A-B)와 (B-A)의 합집합

N, M = map(int, input().split())

A = set(map(int, input().split())) # 집합 한 줄에 입력 받기
B = set(map(int, input().split()))

cha1 = A-B
cha2 = B-A

anw = (cha1 | cha2)
set(anw)

print(len(anw))
