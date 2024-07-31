n = int(input())
dic = {}

for _ in range(n):
    name, log = input().split()
    dic[name] = log # 이름과 로그 상태를 딕셔너리에 저장
    if log == "leave":
        del dic[name]
d = sorted(dic.items(), reverse=True) # 딕셔너리의 항목을 역순으로 정렬
dic = dict(d) # 정렬된 항목을 다시 딕셔너리에 저장

# 딕셔너리의 키(사람 이름)을 출력
for key in dic.keys():
    print(key)