#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬

print(data)
first = data[n-1] #가장 큰 수
print(first)
second = data[n-2] # 두번째로 큰 수
print(second)
print(k)
result1=0
result=0

while True:
    for i in range(k): #가장 큰 수를 K번 더하기
        if m == 0:
            break
        result1 += first
        m -= 1 # 더할때마다 1씩 빼기
    if m==0:
        break
    result += second
    m-=1

print(result, result1)
