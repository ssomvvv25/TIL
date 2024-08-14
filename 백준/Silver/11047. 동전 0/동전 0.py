N, K = map(int, input().split())

coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)
    # coins.append(int(input())) <-- 한 줄로 할 수도 있음

coins.sort(reverse=True) # 편의를 위해 내림차순 정리

ans = 0
for coin in coins:
    if K >= coin:
        ans += K // coin # 몫만큼 더하기
        K %= coin # 나머지 할
        if K <= 0: # 만약 K가 0이면 반복문을 탈출한다.
            break
print(ans)