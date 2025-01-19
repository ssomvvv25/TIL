A,B = map(int,input().split())
C,D = map(int,input().split())

numerator = (B*C+A*D) # 분자
denominator = B*D # 분모

# 최대공약수
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
gcd = gcd(numerator, denominator)

numerator = int(numerator/gcd) # 약분 : 최종 분자는 최대공약수로 나누기
denominator = int(denominator/gcd) # 약분 : 최종 분모는 최대공약수로 나누기

print(f"{numerator} {denominator}")