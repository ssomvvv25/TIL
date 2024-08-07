import sys

N = int(sys.stdin.readline())
names=set()
for i in range(N):
    n1, n2 = input().split()

    if n1 == 'ChongChong' or n2 == 'ChongChong':
        names.add(n1)
        names.add(n2)
    if n1 in names or n2 in names:
        names.add(n1)
        names.add(n2)
print(len(names))


