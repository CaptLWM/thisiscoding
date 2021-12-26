#숫자 카드 게임
n, m = map(int, input().split())

result=0

#한줄씩 입력 받기
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = 10001 #입력받을 수 있는 데이터 범위가 최대 10000이기 때문
    for a in data:
        min_value = min(min_value, a)
    #가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)