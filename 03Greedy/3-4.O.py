#1이 될때까지
# 2<=N<100000, 2<=K<=100000, N>=K
# N이 1이 될때까지 N에서 1을 빼거나 N을 K로 나누어야 하는 최소 횟수

n, k = map(int, input().split())
result=0

#수를 작게 만들기 가장 쉬운방법 : 나누기
while n>=k:
    while n % k != 0:
        n-=1
        result+=1
    n //=k
    result+=1

#마지막으로 남은 수에 대해 1씩 빼기
while n>1:
    n-=1
    result+=1

print(result)
