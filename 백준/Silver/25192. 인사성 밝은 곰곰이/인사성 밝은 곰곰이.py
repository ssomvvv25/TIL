import sys
N = int(sys.stdin.readline())
users=set()
cnt = 0
for _ in range(N):
    user = sys.stdin.readline().strip()
    if user == 'ENTER':
        users.clear()
    else:
        if user not in users:
            cnt += 1
            users.add(user)
print(cnt)