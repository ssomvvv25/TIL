import sys
N = int(sys.stdin.readline())
nums=[]
for i in range(N):
    i = int(sys.stdin.readline())
    nums.append(i)
nums.sort()

fst = round(sum(nums)/N) # 산술평균
print(fst)
sec = nums[N//2] # 중앙값
print(sec)

# 최빈값
dic = dict()
for i in nums: # 빈도수 구하기
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values()) # 빈도수 중 최대값 구하기
mx_dic = [] # 최빈값 숫자를 저장할 배열

for i in dic: # 빈도수 딕셔너리에서
    if mx == dic[i]: # 최빈값이 key 저장
        mx_dic.append(i)
if len(mx_dic) > 1 : # 최빈값이 여러개라면
    print(mx_dic[1]) # 두 번째로 작은 값
else: # 하나라면
    print(mx_dic[0]) # 헤당 값 출력

fourth = nums[-1] - nums[0] # 범위
print(fourth)