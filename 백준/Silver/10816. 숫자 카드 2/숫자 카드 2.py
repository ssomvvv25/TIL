import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

dic = {}

for x in cards:
    if x in dic:
        dic[x] +=1
    else:
        dic[x] = 1
for x in checks:
    if x in dic:
        print(dic[x], end = ' ')
    else:
        print('0', end= ' ')