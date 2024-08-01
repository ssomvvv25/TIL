# 스택을 이용하면 될 듯
import sys
st = [] # 빈 스택

k = int(sys.stdin.readline())

for i in range(k):
    num = int(input())
    if num == 0:
        st.pop()
    else:
        st.append(num)
total = 0
for i in st:
    total += i
print(total)
