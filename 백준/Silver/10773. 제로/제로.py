# 스택 이용
import sys
K = int(sys.stdin.readline())

st = []

for _ in range(K):
    num = int(sys.stdin.readline())

    if num == 0:
        st.pop()
    else:
        st.append(num)
print(sum(st))