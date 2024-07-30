import sys
N, M = map(int,sys.stdin.readline().split())

# S라는 이름의 딕셔너리를 만든다.
S = dict()
cnt = 0

# N개의 문자열을 읽어서 S딕셔너리에 저장
for _ in range(N):
    word = sys.stdin.readline().strip() # 개행 문자 제거
    S[word] = True # 딕셔너리의 키로 문자열을 저장, 값은 True로 설정

# M개의 문자열을 읽어서 S에 포함되어 있는지 확인
for _ in range(M):
    check = sys.stdin.readline().strip() # 개행 문자 제거
    if check in S.keys(): # S 딕셔너리의 키 중에 check가 있는지 확인
        cnt +=1 # 포함되어 있으면 cnt 증가
print(cnt)