import sys
from collections import deque
qu = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        qu.append(com[1])
    elif com[0] == 'pop':
        if qu:
            print(qu.popleft()) # 가장 앞에 있는 정수 빼기
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(qu))
    elif com[0] == 'empty':
        if qu:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if qu:
            print(qu[0]) # 맨 앞 정수 출력
        else:
            print(-1)
    elif com[0] == 'back':
        if qu:
            print(qu[-1])
        else:
            print(-1)