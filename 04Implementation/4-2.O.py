#정수 n 입력
#00시00분00초~n시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수

#정수 입력
n=int(input())
#count 초기화
count=0
# 3찾기
for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i)+str(j)+str(k): #문자열로 변환(00시00분00초=>000000)
                count+=1
print(count)



