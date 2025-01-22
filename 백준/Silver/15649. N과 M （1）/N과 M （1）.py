import sys
input = sys.stdin.readline

def backtracking():
    # 원하는 길이의 순열이 완성되면 출력
    if len(array) == m:
        print(" ".join(map(str,array)))
        return
    # i는 1부터 n까지의 숫자
    for i in range(1,n+1):
        if i not in used:
            array.append(i)
            used.add(i) # set에 추가
            backtracking()
            array.pop()
            used.remove(i) # set에서 제거


n,m = map(int, input().split())
array=[] # 수열을 저장할 리스트
used = set()
backtracking() # 백트래킹 시작