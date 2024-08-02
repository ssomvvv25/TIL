from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) > 1): # 큐에 카드가 한 장 남을 때까지 반복
    deque.popleft() # 큐의 가장 왼쪽(가장 위에 있는) 카드 제거
    move_num = deque.popleft() # 그 다음으로 가장 왼쪽에 있는 카드를 꺼내어 move_num에 저장
    deque.append(move_num) # 방금 꺼낸 move_num을 큐의 맨오른쪽(가장 아래)에 다시 추가
print(deque[0]) # deque[0]은 큐의 가장 왼쪽에 남은 마지막 카드
