import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = [input().rstrip() for _ in range(N)]
see = [input().rstrip() for _ in range(M)]
# 교집합 구하기
ans = list(set(listen) & set(see))
# 오름차순으로 정렬
ans.sort()
print(len(ans))
for a in ans:
    print(a)