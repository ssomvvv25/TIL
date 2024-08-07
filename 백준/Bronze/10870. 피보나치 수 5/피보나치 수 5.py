def fibonachi(n):
    if n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        ans = fibonachi(n-1) + fibonachi(n-2)
    return ans

print(fibonachi(int(input())))