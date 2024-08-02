
while True:
    a = input()
    st = []

    if a == ".":
        break

    for i in a:
        if i == '[' or i == '(':
            st.append(i)
        elif i == ']':
            if len(st) != 0 and st[-1] == '[':
                st.pop() # 맞으면 지워서 스택을 비워줌
            else:
                st.append(']')
                break
        elif i == ')':
            if len(st) != 0 and st[-1] == '(':
                st.pop()
            else:
                st.append(')')
                break
    if len(st) == 0:
        print('yes')
    else:
        print('no')
