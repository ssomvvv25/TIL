# 절댓값 힙

import sys, heapq
N = int(sys.stdin.readline())
arr= []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr,(abs(x),x))