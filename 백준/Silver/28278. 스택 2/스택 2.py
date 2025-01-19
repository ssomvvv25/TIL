import sys

stack = []

n = int(sys.stdin.readline())

for _ in range(n): # 5가지 명령에 대한 코드 작성
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack: # 스택에 정수가 있다면
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == '5':
        if stack:
            print(stack[-1]) # 맨 위의 정수 출력
        else:
            print(-1)

