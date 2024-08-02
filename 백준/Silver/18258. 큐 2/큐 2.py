# 큐
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])

for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0]) # 맨 앞 정수 출력
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])





