from collections import deque
N, K = map(int, input().split())

qu = (deque([i for i in range(1, N+1)]))

# 요세푸스 순열 생성
y = [] # 제거된 사람의 순서를 저장하는 리스트
while len(qu) != 0: # 덱에 사람이 남아 있을 때까지 반복
    for _ in range(K-1):
        qu.append(qu.popleft())
    y.append(str(qu.popleft()))

print('<'+', '.join(y)+'>')