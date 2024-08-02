# 덱
import sys
from collections import deque

N = int(sys.stdin.readline())

d = deque()
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().strip().split()))

    if cmd[0] == 1:
        d.appendleft(cmd[1]) # 덱의 앞에 넣는다.
    elif cmd[0] == 2:
        d.append(cmd[1]) # 덱의 뒤에 넣는다.
    elif cmd[0] == 3:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd[0] == 4:
        if d:
            print(d.pop()) # 맨 뒤의 정수를 빼고 출력한다.
        else:
            print(-1)
    elif cmd[0] == 5:
        print(len(d))
    elif cmd[0] == 6:
        if d:
            print(0)
        else:
            print(1)
    elif cmd[0] == 7:
        if d:
            print(d[0]) # 맨 앞 정수 출력
        else:
            print(-1)
    elif cmd[0] == 8:
        if d:
            print(d[-1]) # 맨 뒤 정수 출력
        else:
            print(-1)




