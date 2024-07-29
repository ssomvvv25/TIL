N = int(input())
words = []

for i in range(N):
    words.append(input())

words = list(set(words)) # 중복 제거
words.sort() # 사전 순서대로 나열
words.sort(key = len) # 길이를 기준으로 나열

for i in words:
    print(i)