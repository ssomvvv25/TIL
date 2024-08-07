cnt = int(input())
yak = list(map(int, input().split()))

yak.sort()
print(yak[0]*yak[-1])