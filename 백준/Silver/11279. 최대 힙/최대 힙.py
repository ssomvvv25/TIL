# 힙 함수
import sys, heapq
# heapq모듈은 최소힙 --> 그러므로 최대힙을 구현하려면 뭘 해줘야함!
N = int(input())
max_heap = []
for i in range(N):
    x = int(sys.stdin.readline()) * -1
    if x == 0:
        if max_heap:
            print(heapq.heappop(max_heap)*-1)
        else:
            print(0)
    else:
        heapq.heappush(max_heap, x)