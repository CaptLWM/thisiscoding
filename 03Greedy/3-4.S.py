#1이 될때까지
# 2<=N<100000, 2<=K<=100000, N>=K
# N이 1이 될때까지 N에서 1을 빼거나 N을 K로 나누어야 하는 최소 횟수

n, k = map(int, input().split())
result=0

while True:
    # (N==K 로 나누어떨어지는 수) 될때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    # N이 K 보다 작을 때(더이상 나눌 수 없을 때) break
    if n<k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1식 빼기
result += (n-1)
print(result)